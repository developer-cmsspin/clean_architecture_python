from abc import ABCMeta, abstractclassmethod

from kink import inject
from domain.model.list_test import ListTest

import array as arr


@inject
class ILisTestInfrastructure(metaclass=ABCMeta):
    @abstractclassmethod
    async def execute(self) -> ListTest:
        pass
