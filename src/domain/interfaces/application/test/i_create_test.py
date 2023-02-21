from abc import ABCMeta, abstractclassmethod
from domain.dto.test_dto import TestDto


class ICreateTest(metaclass=ABCMeta):
    @abstractclassmethod
    def handler(self, request: TestDto):
        pass
