from fastapi import APIRouter

from src.controllers.printer_controller import PrinterController
from src.request.request import OrderDetailRequest
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
