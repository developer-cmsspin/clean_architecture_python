from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from kink import di
from src.domain.dto.list_test_dto import ListTestDto
from src.domain.dto.test_dto import TestDto
from src.domain.interfaces.application.test.i_create_test import ICreateTest
from src.domain.interfaces.application.test.i_get_test import IGetTest


router = APIRouter(
    prefix="/test",
    tags=["my items"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}
fake_items_db_detail = {"plumbus": {"name": "Plumbus"}}


@router.get("/list")
async def list():
    application: IGetTest = di[IGetTest]
    result = await application.handler()
    return JSONResponse(content=jsonable_encoder(result))


@router.post("/create")
async def create(request: TestDto):
    application: ICreateTest = di[ICreateTest]
    result = await application.handler(request)
    return JSONResponse(content=jsonable_encoder(result))


@router.get("/detail/{{item_id}}", tags=["detail"],  responses={403: {"description": "Operation forbidden"}})
async def detail(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return fake_items_db_detail
