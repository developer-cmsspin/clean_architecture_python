from dataclasses import dataclass


class Test():

    def __init__(self, name: str, code: int, company: str) -> None:
        self.name = name
        self.code = code
        self.company = company

    name: str
    code: int
    company: str
