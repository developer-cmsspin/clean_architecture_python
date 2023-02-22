from kink import di

from domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from infrastructure.persistence.repository.repository_test import RepositoryTest


def add_persistence() -> None:
    di[IRepositoryTest] = RepositoryTest()
