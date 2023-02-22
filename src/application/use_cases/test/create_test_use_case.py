from automapper import mapper
from domain.dto.test_dto import TestDto
from domain.interfaces.application.test.i_create_test import ICreateTest
from domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from domain.model.test import Test


class CreateTestUseCase(ICreateTest):

    __repository: IRepositoryTest

    def __init__(self, repository: IRepositoryTest) -> None:
        self.__repository = repository

    async def handler(self, request: TestDto) -> TestDto:
        test_data: Test = mapper.map(request)
        result: Test = await self.__repository.create_test(test_data)
        return mapper.map(result)
