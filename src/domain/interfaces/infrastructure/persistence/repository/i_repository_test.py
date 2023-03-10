from abc import ABC, abstractclassmethod
from typing import List
from src.domain.model.test import Test
import array as arr


class IRepositoryTest():
    @abstractclassmethod
    async def create_test(self, test: Test) -> Test:
        pass

    @abstractclassmethod
    async def get_all() -> list[Test]:
        pass
