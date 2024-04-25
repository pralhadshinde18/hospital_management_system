from database import SessionLocal
from model.hospital_model import Hospital
from schema.hospital_details_schema import HospitalDetailsResponse
from fastapi import HTTPException


class HospitalDetailsRepository:
    def get_hospital_details(self, hospital_id: int) -> HospitalDetailsResponse:
        db = SessionLocal()
        hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
        if not hospital:
            db.close()
            raise HTTPException(status_code=404, detail="Hospital not found")

        technicians = [
            {
                "id": technician.id,
                "user_name": technician.user_name,
                "name": technician.name,
                "hospital_name": technician.hospital_name,
                "address": technician.address,
                "contact_number": technician.contact_number,
                "whatsapp_number": technician.whatsapp_number,
                "email_address": technician.email_address,
                "education": technician.education,
                "gender": technician.gender,
                "description": technician.description

            }
            for technician in hospital.technicians
        ]
        patients = [
            {
                "id": patient.id,
                "name": patient.name,
                "address": patient.address,
                "contact_number": patient.contact_number,
                "whatsapp_number": patient.whatsapp_number,
                "age": patient.age,
                "gender": patient.gender,

                "reference_by": patient.reference_by,
                "test_conducted_by": patient.test_conducted_by,
                "test_hospital": patient.test_hospital,
                "referred_doctor": patient.referred_doctor,
                "referred_hospital": patient.referred_hospital,
                "clinical_category": patient.clinical_category,
                "clinical_sub_category": patient.clinical_sub_category,
                "test": patient.test,
                "format": patient.format,
                "exam_procedure": patient.exam_procedure

            }
            for patient in hospital.patients
        ]

        db.close()

        return HospitalDetailsResponse(
            hospital_name=hospital.hospital_name,
            technicians=technicians,
            patients=patients
        )
