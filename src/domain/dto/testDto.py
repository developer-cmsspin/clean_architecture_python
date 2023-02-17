from dataclasses import dataclass


@dataclass(frozen=True)
class TestDto():
    name: str
    code: int
