# bootstrap.py
# https://www.netguru.com/blog/dependency-injection-with-python-make-it-easy
# https://pypi.org/project/kink/
# https://ellibrodepython.com/abstract-base-class

from kink import di
from automapper import mapper, Mapper
from src.application.configuration.mapping.test_mapper_configuration import test_mapper_config
from src.application.use_cases.test.create_test_use_case import CreateTestUseCase
from src.domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure
from src.domain.interfaces.application.test.i_create_test import ICreateTest
from src.application.use_cases.test.get_test_use_case import GetTestUseCase
from src.domain.interfaces.application.test.i_get_test import IGetTest
from src.domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest


def add_application() -> None:
    test_mapper_config()
    di[Mapper] = mapper
    di[IGetTest] = GetTestUseCase(di[ILisTestInfrastructure])
    di[ICreateTest] = CreateTestUseCase(di[IRepositoryTest], di[Mapper])
