# bootstrap.py
# https://www.netguru.com/blog/dependency-injection-with-python-make-it-easy
# https://pypi.org/project/kink/
# https://ellibrodepython.com/abstract-base-class

from kink import di
from infrastructure.external.test.access_service_infrastructure import AccessServiceInfrastructure

from domain.interfaces.infrastructure.external.test.i_access_service import IAccessService


def add_infrastructure_external() -> None:
    di[IAccessService] = AccessServiceInfrastructure()
