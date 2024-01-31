"""Controller"""
from dotenv import dotenv_values

from src.controllers.rest_controller import RestController
from src.models.ks_order_model import KsOrderModel
from src.models.ks_roller_model import KsRollerModel
from src.models.ks_order_ean_model import KsOrderEanModel
from src.printer.printer import Printer
from src.request.request import OrderDetailRequest, RolerRequest, OrderDetailEanRequest
from src.exceptions.printer_exception import PrinterException

config: dict = dotenv_values(".env")


class PrinterController(RestController):
    """PrinterController"""

    def print_order_detail(self, request: OrderDetailRequest):
        """print_order_detail"""
        try:
            printer = Printer(request.ip, int(config["PRINTER_PORT"])  if request.printer == 1 else int(config["PRINTER_PORT_2"]),
                              KsOrderModel(request.detail_id, request.client_name, request.ref,
                                           request.color, request.mts, request.kg, request.person))
            res = printer.print_code(printer.coder.build_label_code())
            # res = printer.print()
            if not res['ok']:
                raise PrinterException(res['error'])
            return self.build_ok_response_with_data("Ready")
        except PrinterException as e:
            return self.build_error_response(str(e))

    def print_rol(self, request: RolerRequest):
        """print_rol"""
        try:
            printer = Printer(request.ip, int(config["PRINTER_PORT"])  if request.printer == 1 else int(config["PRINTER_PORT_2"]),
                              KsRollerModel(request.mts, request.ref, request.color,
                                            request.person, request.desc, request.detail_id))
            res = printer.print_code(printer.coder.build_roler_code())
            # res = printer.print_rol()
            if not res['ok']:
                raise PrinterException(res['error'])
            return self.build_ok_response_with_data("Ready")
        except PrinterException as e:
            return self.build_error_response(str(e))
        
    def print_order_nalsani_detail(self, request: OrderDetailEanRequest):
        """print_order_detail"""
        try:
            printer = Printer(request.ip, int(config["PRINTER_PORT"])  if request.printer == 1 else int(config["PRINTER_PORT_2"]),
                              KsOrderEanModel(request.detail_id, request.client_name, request.ref,
                                           request.color, request.mts, request.kg, request.person,
                                           request.client_cod, request.ref_description, request.ean, request.oc))
            res = printer.print_code(printer.coder.build_nalsani_code())
            if not res['ok']:
                raise PrinterException(res['error'])
            return self.build_ok_response_with_data("Ready")
        except PrinterException as e:
            return self.build_error_response(str(e))
    
    def print_order_eliot_detail(self, request: OrderDetailEanRequest):
        """print_order_detail"""
        try:
            printer = Printer(request.ip, int(config["PRINTER_PORT"])  if request.printer == 1 else int(config["PRINTER_PORT_2"]),
                              KsOrderEanModel(request.detail_id, request.client_name, request.ref,
                                           request.color, request.mts, request.kg, request.person,
                                           request.client_cod, request.ref_description, request.ean, request.oc))
            code = printer.coder.build_eliot_code() if request.client_cod == 'MAN0024' else printer.coder.build_large_code()
            res = printer.print_code(code)
            if not res['ok']:
                raise PrinterException(res['error'])
            return self.build_ok_response_with_data("Ready")
        except PrinterException as e:
            return self.build_error_response(str(e))
