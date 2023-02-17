from kink import di
from infrastructure.external.dependency_injection import add_infrastructure_external
from application.dependency_injection import add_application
import asyncio

from presentation.common.program_console import ProgramConsole

add_infrastructure_external()
add_application()


if __name__ == '__main__':
    console = ProgramConsole()
    asyncio.run(console.run())
    # print(type(di[ICreateTest]))
    # create_test: ICreateTest = di[ICreateTest]
    # print(type(create_test))
    # request: TestDto = TestDto("aaa", 12312)
    # aaa = create_test.handler(request)
    # print("OK")
