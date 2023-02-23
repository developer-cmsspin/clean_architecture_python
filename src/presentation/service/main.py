from kink import di
from src.infrastructure.external.dependency_injection import add_infrastructure_external
from src.application.dependency_injection import add_application
import asyncio

# from src.presentation.common.program_console import run_console

add_infrastructure_external()
add_application()


if __name__ == '__main__':
    asyncio.run(run_console())
    # print(type(di[ICreateTest]))
    # create_test: ICreateTest = di[ICreateTest]
    # print(type(create_test))
    # request: TestDto = TestDto("aaa", 12312)
    # aaa = create_test.handler(request)
    # print("OK")
