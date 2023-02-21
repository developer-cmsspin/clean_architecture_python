from abc import ABC, abstractclassmethod
from typing import List
from domain.model.test import Test
import array as arr


class RepositoryTest():
    @abstractclassmethod
    async def create_test(self, test: Test):
        pass

    @abstractclassmethod
    async def get_all() -> list[Test]:
        pass
