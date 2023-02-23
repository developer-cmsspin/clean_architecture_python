from fastapi import FastAPI
from src.presentation.api.routers import test
from src.infrastructure.external.dependency_injection import add_infrastructure_external
from src.infrastructure.persistence.dependency_injection import add_persistence
from src.application.dependency_injection import add_application

app = FastAPI()
app.include_router(test.router)

# init DI
add_infrastructure_external()
add_persistence()
add_application()
