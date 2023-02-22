from domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from domain.model.test import Test


class RepositoryTest(IRepositoryTest):

    async def create_test(self, test: Test) -> Test:
        return test

    async def get_all() -> list[Test]:
        return list[Test]()
