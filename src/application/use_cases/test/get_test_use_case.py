from kink import inject
from automapper import mapper
from src.domain.dto.test_dto import TestDto
from src.domain.interfaces.application.test.i_get_test import IGetTest
from src.domain.dto.list_test_dto import ListTestDto
from src.domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure

# conectar la persistencia
# crear paquetes pip3
# validar el singleton y el transient DI


@inject
class GetTestUseCase(IGetTest):
    __test_infrastructure: ILisTestInfrastructure

    def __init__(self, test_infrastructure: ILisTestInfrastructure) -> None:
        (self.__test_infrastructure) = test_infrastructure

    async def handler(self) -> ListTestDto:
        api_result = await self.__test_infrastructure.execute()
        return mapper.to(ListTestDto).map(api_result)
