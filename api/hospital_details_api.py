from fastapi import APIRouter
from service.hospital_details_service import HospitalDetailsService
from schema.hospital_details_schema import HospitalDetailsResponse

router = APIRouter()


@router.get("/hospital/{hospital_id}/details", response_model=HospitalDetailsResponse)
def get_hospital_details(hospital_id: int):
    hospital_details_service = HospitalDetailsService()
    hospita_details = hospital_details_service.get_hospital_details(hospital_id)
    return hospita_details
