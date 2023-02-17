# bootstrap.py
# https://www.netguru.com/blog/dependency-injection-with-python-make-it-easy
# https://pypi.org/project/kink/
# https://ellibrodepython.com/abstract-base-class

from kink import di
from domain.interfaces.infrastructure.external.test.i_access_service import IAccessService
from domain.interfaces.application.test.i_create_test import ICreateTest
from application.use_cases.test.create_test_use_case import CreateTestUseCase


def add_application() -> None:
    di[ICreateTest] = CreateTestUseCase(di[IAccessService])
