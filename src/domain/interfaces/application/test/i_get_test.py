from abc import ABCMeta, abstractclassmethod
from src.domain.dto.list_test_dto import ListTestDto


class IGetTest(metaclass=ABCMeta):
    @abstractclassmethod
    async def handler(self) -> ListTestDto:
        pass
