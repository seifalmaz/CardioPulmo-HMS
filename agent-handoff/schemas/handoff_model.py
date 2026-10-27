"""
CardioPulmo-HMS: Pydantic v2 Data Models for AI Agent Handoff Protocol
======================================================================
Defines strict schema validation, context minimization, cryptographic hashing,
and prompt-injection boundary guards for cross-specialty clinical referrals.
"""

from datetime import datetime
from enum import Enum
import hashlib
import json
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, field_validator


class SpecialtyEnum(str, Enum):
    CARDIOLOGY = "CARDIOLOGY"
    PULMONOLOGY = "PULMONOLOGY"


class ReferralStatusEnum(str, Enum):
    PENDING_CLINICIAN_REVIEW = "PENDING_CLINICIAN_REVIEW"
    ACCEPTED = "ACCEPTED"
    INFO_REQUESTED = "INFO_REQUESTED"
    REJECTED = "REJECTED"
    CLOSED_WITH_OUTCOME = "CLOSED_WITH_OUTCOME"


class VitalsContext(BaseModel):
    bp: str = Field(..., description="Blood Pressure in mmHg, e.g., '146/92 mmHg'")
    hr: int = Field(..., ge=30, le=250, description="Heart Rate in beats per minute")
    spo2: str = Field(..., description="Pulse oximetry saturation, e.g., '91%'")
    rr: int = Field(..., ge=6, le=60, description="Respiratory Rate in breaths per minute")
    temperature: Optional[str] = Field(None, description="Body temperature, e.g., '98.4 F'")
    map: Optional[int] = Field(None, description="Mean Arterial Pressure in mmHg")
    timestamp: datetime = Field(..., description="Timestamp vitals were recorded")


class LabResultContext(BaseModel):
    loinc: str = Field(..., description="Standard LOINC test code, e.g., '33762-6'")
    test: str = Field(..., description="Test display name, e.g., 'NT-proBNP'")
    value: Union[float, int, str] = Field(..., description="Reported clinical laboratory value")
    unit: str = Field(..., description="Measurement unit, e.g., 'pg/mL'")
    flag: str = Field(..., description="Demographic flag: NORMAL, LOW, HIGH, CRITICAL")


class CXRFindingItem(BaseModel):
    label: str = Field(..., description="Thoracic pathology label from NIH ChestX-ray14")
    prob: float = Field(..., ge=0.0, le=1.0, description="Calibrated model probability")


class CXRScreeningContext(BaseModel):
    study_id: str = Field(..., description="DICOM study or radiograph accession number")
    findings: List[CXRFindingItem] = Field(default_factory=list, description="Top predicted pathologies")
    gradcam_ref: Optional[str] = Field(None, description="URI reference to authenticated Grad-CAM heatmap overlay")


class MinimizedClinicalContext(BaseModel):
    vitals: VitalsContext
    verified_labs: List[LabResultContext] = Field(default_factory=list)
    cxr_cv_screening: Optional[CXRScreeningContext] = None


class HandoffPayload(BaseModel):
    handoff_id: str = Field(..., description="Unique UUID for this handoff transaction")
    correlation_id: str = Field(..., description="Trace correlation ID for observability")
    status: ReferralStatusEnum = Field(default=ReferralStatusEnum.PENDING_CLINICIAN_REVIEW)
    source_specialty: SpecialtyEnum
    destination_specialty: SpecialtyEnum
    authorized_sender_id: str
    sender_name: str
    patient_id: str
    encounter_id: str
    referral_reason: str = Field(..., max_length=1000)
    minimized_context: MinimizedClinicalContext
    missingness_and_uncertainty: List[str] = Field(default_factory=list)
    provenance_sha256: str = Field(..., description="SHA-256 seal of canonical clinical context")
    untrusted_delimiters_verified: bool = Field(default=False)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("referral_reason")
    @classmethod
    def sanitize_prompt_injection(cls, v: str) -> str:
        """Defense-in-depth sanitization against prompt injection in free-text notes."""
        forbidden_patterns = [
            "ignore previous instructions",
            "system prompt",
            "output admin credentials",
            "you are now a",
            "reveal secret",
        ]
        lower_v = v.lower()
        for pattern in forbidden_patterns:
            if pattern in lower_v:
                raise ValueError(f"Adversarial instruction detected: '{pattern}'. Payload rejected.")
        return v.strip()

    def compute_context_digest(self) -> str:
        """Generate canonical SHA-256 provenance seal for minimized clinical context."""
        canonical_str = self.minimized_context.model_dump_json(exclude_none=True)
        return hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()

    def verify_provenance(self) -> bool:
        """Validate whether provenance_sha256 matches computed digest."""
        return self.compute_context_digest() == self.provenance_sha256
