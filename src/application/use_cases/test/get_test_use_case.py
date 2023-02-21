from kink import inject
from automapper import mapper
from domain.dto.test_dto import TestDto
from domain.interfaces.application.test.i_get_test import IGetTest
from domain.dto.list_test_dto import ListTestDto
from domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure

# conectar la persistencia
# crear paquetes pip3
# validar el singleton y el transient DI


@inject
class GetTestUseCase(IGetTest):
    __api_service: ILisTestInfrastructure

    def __init__(self, api_service: ILisTestInfrastructure) -> None:
        (self.__api_service) = (api_service)

    async def handler(self) -> ListTestDto:
        api_result = await self.__api_service.execute()
        return mapper.to(ListTestDto).map(api_result)
