from dataclasses import dataclass
from typing import List
from domain.dto.test_dto import TestDto


@dataclass(frozen=True)
class ListTestDto():
    items: list[TestDto]
