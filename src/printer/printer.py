import socket

from src.models.zpl_model import ZplModel
from src.printer.zpl_code import ZplCoder


class Printer:

    def __init__(self, printer_ip: str, printer_port: int, zpl_model: ZplModel):
        self.printer_ip = printer_ip
        self.printer_port = printer_port
        self.coder = ZplCoder(zpl_model)

    def print(self):
        print(self.printer_ip)
        print(self.printer_port)
        addr = (self.printer_ip, self.printer_port)
        payload = self.coder.build_label_code()
        print(payload)
        s = socket.socket()
        res = {'ok': True, "msg": '', 'error': ''}
        try:
            s.settimeout(5)
            s.connect(addr)
            s.settimeout(None)
            s.send(payload)
            res['msg'] = 'Ready'
        except Exception as e:
            print(str(e))
            res['ok'] = False
            res['error'] = str(e)
        finally:
            if s is not None:
                s.close()
            return res
