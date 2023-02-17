from domain.dto.testDto import TestDto
from domain.interfaces.application.test.i_create_test import ICreateTest
from domain.interfaces.infrastructure.external.test.i_access_service import IAccessService
from kink import inject


@inject
class CreateTestUseCase(ICreateTest):

    _access_service: IAccessService

    def __init__(self, access_service: IAccessService) -> None:
        (self._access_service) = (access_service)

    def handler(self, request: TestDto):
        self._access_service.execute(request)
        print("OK")
