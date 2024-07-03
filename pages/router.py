from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

import asyncio

from api.depends import generaldata_service, metrics_service

from services.generaldata import GeneralDataService

from typing import Annotated

router = APIRouter(
    prefix="/pages",
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_page(request: Request, general_service: Annotated[GeneralDataService, Depends(generaldata_service)]):
    data = asyncio.run(general_service.get_all())
    return templates.TemplateResponse("base.html", {"request": request, "data": data})

@router.get("/home")
def get_home(request: Request, general_service: Annotated[GeneralDataService, Depends(generaldata_service)]):
    data = asyncio.run(general_service.get_all())
    return templates.TemplateResponse("home.html", {"request": request, "data": data})