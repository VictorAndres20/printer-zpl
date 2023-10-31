from fastapi import APIRouter

from src.controllers.printer_controller import PrinterController
from src.request.request import OrderDetailRequest, RolerRequest
from src.request.response import Response

controller = PrinterController()

router = APIRouter(
    prefix="/printer",
    responses={
        404: {"Description": "Not found"}
    }
)


@router.post("/print")
async def save(request: OrderDetailRequest) -> Response:
    return controller.print(request)


@router.post("/print-rol")
async def save(request: RolerRequest) -> Response:
    return controller.print_rol(request)
