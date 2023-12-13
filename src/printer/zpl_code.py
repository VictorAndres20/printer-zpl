from src.models.zpl_model import ZplModel
from src.utils.date_formatter import build_date, build_date_eliot
from src.utils.eliot_barcode import build_eliot_barcode


class ZplCoder:

    def __init__(self, model: ZplModel):
        self.model = model

    def build_label_code(self):
        code = (f"^XA^CI28^FX Third section with bar code.^BY2,3,100^FO30,10^BC^FD{self.model.id_barcode}^FS^FO50,150"
                f"^GB300,3,3^FS^FX Second section with recipient address and permit information."
                f"^CFA,14^FO50,170^FD{self.model.label1}^FS^FO50,190^FD{self.model.label2}^FS"
                f"^FO50,210^FD{self.model.label3}^FS^FO50,230^FD{self.model.label4}^FS"
                f"^FO50,250^FD{self.model.label5}^FS^FO50,270^FD{self.model.label6}^FS^XZ")
        return code

    def build_roler_code(self):
        code = (f"^XA"
                f"^GB300,3,3^FS^FX Second section with recipient address and permit information."
                f"^CFA,14^FO50,170^FD{self.model.id_barcode}^FS^FO50,190^FD{self.model.label1}^FS"
                f"^FO50,210^FD{self.model.label2}^FS^FO50,230^FD{self.model.label3}^FS"
                f"^FO50,250^FD{self.model.label4}^FS^FO50,270^FD{self.model.label5}^FS^XZ")
        return code

    def build_nalsani_code(self):
        code = (f"^XA^CI28^FX Third section with bar code.^BY2,3,100^FO30,10^BC^FD{self.model.ean}^FS^FO50,150"
                f"^GB300,3,3^FS^FX Second section with recipient address and permit information."
                f"^CFA,14^FO50,170^FD{self.model.label1}^FS^FO50,190^FD{self.model.label8}^FS"
                f"^FS^FO50,210^FD{self.model.label2}^FS"
                f"^FO50,230^FD{self.model.label3}^FS^FO50,250^FD{self.model.label4}^FS"
                f"^FS^FO50,270^FD{build_date()}  {self.model.label6}^FS^XZ")
        return code

    def build_eliot_code(self):
        code = f"^XA^FXinformation.^CFA,14"
        code += f"^FO50,10^FD{build_date_eliot()} {self.model.label2}{self.model.label3}^FS"
        code += f"^FO520,10^FD{self.model.label2}^FS"
        code += f"^FO680,10^FD{self.model.ean}^FS"
        code += f"^FO50,35^FDCOLOR: {self.model.label3} OC:{self.model.oc}^FS"
        code += f"^FO680,35^FD{self.model.label4}.00 MTS^FS"
        code += f"^CI28^FXbar code."
        code += f"^BY2,3,100^FO30,60^BC^FD1{self.model.ean}3{build_eliot_barcode(self.model.label4)}.000:    ^FS^XZ"
        return code
