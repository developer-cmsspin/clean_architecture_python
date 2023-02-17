from abc import ABCMeta, abstractclassmethod
from domain.dto.testDto import TestDto


class ICreateTest(metaclass=ABCMeta):
    @abstractclassmethod
    def handler(self, request: TestDto):
        pass
