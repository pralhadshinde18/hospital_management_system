from schema.hospital_details_schema import HospitalDetailsResponse
from repository.hospital_details_repo import HospitalDetailsRepository


class HospitalDetailsService:
    def __init__(self):
        self.repo = HospitalDetailsRepository()

    def get_hospital_details(self, hospital_id: int) -> HospitalDetailsResponse:
        return self.repo.get_hospital_details(hospital_id)