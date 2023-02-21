# bootstrap.py
# https://www.netguru.com/blog/dependency-injection-with-python-make-it-easy
# https://pypi.org/project/kink/
# https://ellibrodepython.com/abstract-base-class

from kink import di
from application.configuration.mapping.test_mapper_configuration import test_mapper_config
from domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure
from domain.interfaces.application.test.i_create_test import ICreateTest
from application.use_cases.test.create_test_use_case import CreateTestUseCase
from application.use_cases.test.get_test_use_case import GetTestUseCase
from domain.interfaces.application.test.i_get_test import IGetTest


def add_application() -> None:
    test_mapper_config()
    di[ICreateTest] = CreateTestUseCase(di[ILisTestInfrastructure])
    di[IGetTest] = GetTestUseCase(di[ILisTestInfrastructure])
