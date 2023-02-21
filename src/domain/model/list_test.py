from typing import List
from dataclasses import dataclass

from domain.model.test import Test


class ListTest():
    items: list[Test]
