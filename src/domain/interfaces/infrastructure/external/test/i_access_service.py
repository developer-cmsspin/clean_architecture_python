from abc import ABCMeta, abstractclassmethod

from kink import inject
from domain.model.test import Test
import array as arr


@inject
class IAccessService(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(self, test: Test) -> Test:
        pass
