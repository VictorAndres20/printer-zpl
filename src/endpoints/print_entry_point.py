"""Function printing python version."""
from fastapi import APIRouter

from src.controllers.printer_controller import PrinterController
from src.request.request import OrderDetailRequest, RolerRequest, OrderDetailEanRequest
from src.request.response import Response

controller = PrinterController()

router = APIRouter(
    prefix="/printer",
    responses={
        404: {"Description": "Not found"}
    }
)


@router.post("/print")
async def print_box(request: OrderDetailRequest) -> Response:
    """Function printing python version."""
    return controller.print_order_detail(request)
    # return Response(ok=True)


@router.post("/print-rol")
async def print_roller(request: RolerRequest) -> Response:
    """Function printing python version."""
    return controller.print_rol(request)
    # return Response(ok=True)

@router.post("/print-nalsani-rol")
async def print_roller_nalsani(request: OrderDetailEanRequest) -> Response:
    """Function printing python version."""
    return controller.print_order_nalsani_detail(request)
    # return Response(ok=True)

@router.post("/print-eliot-rol")
async def print_roller_eliot(request: OrderDetailEanRequest) -> Response:
    """Function printing python version."""
    return controller.print_order_eliot_detail(request)
    # return Response(ok=True)
