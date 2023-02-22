from fastapi import FastAPI
from infrastructure.persistence.dependency_injection import add_persistence
from presentation.api.routers import test
from infrastructure.external.dependency_injection import add_infrastructure_external
from application.dependency_injection import add_application

app = FastAPI()
app.include_router(test.router)

# init DI
add_infrastructure_external()
add_persistence()
add_application()
