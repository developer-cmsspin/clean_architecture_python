from kink import inject

from src.domain.interfaces.application.test.i_create_test import ICreateTest


@inject
class TestService():
    __create_test: ICreateTest = None

    def __init__(self, create_test: ICreateTest) -> None:
        (self.__create_test) = (create_test)

    def handler():
        print("OK")
