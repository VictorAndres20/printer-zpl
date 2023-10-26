from src.controllers.rest_controller import RestController
from src.models.ks_order_model import KsOrderModel
from src.printer.printer import Printer
from src.request.request import OrderDetailRequest
from dotenv import dotenv_values
config = dotenv_values(".env")


class PrinterController(RestController):

    def print(self, request: OrderDetailRequest):
        try:
            printer = Printer(config["PRINTER_IP"], int(config["PRINTER_PORT"]),
                              KsOrderModel(request.detail_id, request.client_name, request.ref,
                                           request.color, request.mts, request.kg, request.person))
            res = printer.print()
            if not res['ok']:
                raise Exception(res['error'])
            return self.build_ok_response_with_data("Ready")
        except Exception as e:
            return self.build_error_response(str(e))
