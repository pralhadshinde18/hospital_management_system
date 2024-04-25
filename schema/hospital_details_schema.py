from pydantic import BaseModel
from typing import List, Optional


class Technician(BaseModel):
    id: int
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: int
    whatsapp_number: int
    email_address: str
    education: str
    gender: str
    description: str


class Patient(BaseModel):
    id: int
    name: str
    address: str
    contact_number: int
    whatsapp_number: int
    age: int
    gender: str
    reference_by: str
    test_conducted_by: str
    test_hospital: str
    referred_doctor: str
    referred_hospital: str
    clinical_category: str
    clinical_sub_category: str
    test: str
    format: str
    exam_procedure: str


class HospitalDetailsResponse(BaseModel):
    hospital_name: str
    technicians: List[Technician]
    patients: List[Patient]
