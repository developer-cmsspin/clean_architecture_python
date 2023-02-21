from abc import ABCMeta, abstractclassmethod
from domain.dto.list_test_dto import ListTestDto


class IGetTest(metaclass=ABCMeta):
    @abstractclassmethod
    async def handler(self) -> ListTestDto:
        pass
