# bootstrap.py
# https://www.netguru.com/blog/dependency-injection-with-python-make-it-easy
# https://pypi.org/project/kink/
# https://ellibrodepython.com/abstract-base-class

from kink import di
from src.infrastructure.external.test.list_test_infrastructure import ListTestInfrastructure

from src.domain.interfaces.infrastructure.external.test.i_list_test_infrastructure import ILisTestInfrastructure


def add_infrastructure_external() -> None:
    di[ILisTestInfrastructure] = ListTestInfrastructure()
