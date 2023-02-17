from domain.model.test import Test
from domain.interfaces.infrastructure.external.test.i_access_service import IAccessService


class AccessServiceInfrastructure(IAccessService):
    def execute(self, test: Test) -> Test:
        print("OK")
