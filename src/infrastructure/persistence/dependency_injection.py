from kink import di

from src.domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from src.infrastructure.persistence.repository.repository_test import RepositoryTest


def add_persistence() -> None:
    di[IRepositoryTest] = RepositoryTest()
