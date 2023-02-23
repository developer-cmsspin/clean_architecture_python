from typing import List
from src.domain.model.list_test import ListTest
from src.domain.model.test import Test
from src.domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure


class ListTestInfrastructure(ILisTestInfrastructure):
    async def execute(self) -> ListTest:
        result = ListTest()
        result.items = list[Test]()
        result.items.append(Test("Andres", 33, "My Company"))
        return result
