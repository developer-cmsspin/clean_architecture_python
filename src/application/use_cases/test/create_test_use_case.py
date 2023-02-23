from automapper import Mapper
from src.domain.dto.test_dto import TestDto
from src.domain.interfaces.application.test.i_create_test import ICreateTest
from src.domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from src.domain.model.test import Test


class CreateTestUseCase(ICreateTest):

    __repository: IRepositoryTest
    __mapper: Mapper

    def __init__(self, repository: IRepositoryTest, mapper: Mapper) -> None:
        (self.__repository, self.__mapper) = (repository, mapper)

    async def handler(self, request: TestDto) -> TestDto:
        test_data: Test = self.__mapper.map(request)
        result: Test = await self.__repository.create_test(test_data)
        return self.__mapper.map(result)
