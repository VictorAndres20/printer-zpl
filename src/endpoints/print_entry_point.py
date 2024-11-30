from fastapi import APIRouter

from src.controllers.printer_controller import PrinterController
from src.request.request import OrderDetailRequest, RolerRequest, OrderDetailEanRequest
from src.request.response import Response
from dotenv import dotenv_values

config = dotenv_values(".env")

controller = PrinterController()

router = APIRouter(
    prefix="/printer",
    responses={
        404: {"Description": "Not found"}
    }
)


@router.post("/print")
async def print_box(request: OrderDetailRequest) -> Response:
    if config['ENV'] == 'dev':
        return Response(ok=True, message='Process Finished', data={})
    return controller.print_order_detail(request)


@router.post("/print-rol")
async def print_roller(request: RolerRequest) -> Response:
    if config['ENV'] == 'dev':
        return Response(ok=True, message='Process Finished', data={})
    return controller.print_rol(request)


@router.post("/print-nalsani-rol")
async def print_roller_nalsani(request: OrderDetailEanRequest) -> Response:
    if config['ENV'] == 'dev':
        return Response(ok=True, message='Process Finished', data={})
    return controller.print_order_nalsani_detail(request)


@router.post("/print-reymond-rol")
async def print_roller_reymond(request: OrderDetailEanRequest) -> Response:
    if config['ENV'] == 'dev':
        return Response(ok=True, message='Process Finished', data={})
    return controller.print_order_reymond_detail(request)


@router.post("/print-eliot-rol")
async def print_roller_eliot(request: OrderDetailEanRequest) -> Response:
    if config['ENV'] == 'dev':
        return Response(ok=True, message='Process Finished', data={})
    return controller.print_order_eliot_detail(request)
