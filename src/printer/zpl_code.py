from src.models.zpl_model import ZplModel
from src.utils.date_formatter import build_date, build_date_eliot
from src.utils.eliot_barcode import build_eliot_barcode
from dotenv import dotenv_values

config = dotenv_values(".env")


class ZplCoder:

    def __init__(self, model: ZplModel):
        self.model = model

    def build_label_code(self):
        code = (f"^XA^CI28^FX Third section with bar code.^BY2,3,100^FO{config['LABEL_WIDTH_BOX']},10^BC^FD{self.model.id_barcode}^FS^FO{config['LABEL_WIDTH_BOX']},150"
                f"^GB300,3,3^FS^FX Second section with recipient addres and permit information."
                f"^CFA,14^FO{config['LABEL_WIDTH_BOX']},170^FD{self.model.label1}^FS^FO{config['LABEL_WIDTH_BOX']},190^FD{self.model.label2}^FS"
                f"^FO{config['LABEL_WIDTH_BOX']},210^FD{self.model.label3}^FS^FO{config['LABEL_WIDTH_BOX']},230^FD{self.model.label4}^FS"
                f"^FO{config['LABEL_WIDTH_BOX']},250^FD{self.model.label5}^FS^FO{config['LABEL_WIDTH_BOX']},270^FD{self.model.label6}^FS^XZ")
        return code

    def build_roler_code(self):
        code = (f"^XA"
                f"^GB300,3,3^FS^FX Second section with recipient address and permit information."
                f"^CFA,14^FO{config['LABEL_WIDTH_ROLLER']},170^FD{self.model.id_barcode}^FS^FO{config['LABEL_WIDTH_ROLLER']},190^FD{self.model.label1}^FS"
                f"^FO{config['LABEL_WIDTH_ROLLER']},210^FD{self.model.label2}^FS^FO{config['LABEL_WIDTH_ROLLER']},230^FD{self.model.label3}^FS"
                f"^FO{config['LABEL_WIDTH_ROLLER']},250^FDMts: {self.model.label4}^FS^FO{config['LABEL_WIDTH_ROLLER']},270^FD{self.model.label5}^FS^XZ")
        return code

    def build_nalsani_code(self):
        code = (f"^XA^CI28^FX Third section with bar code.^BY2,3,100^FO{config['LABEL_WIDTH_ROLLER_N']},10^BC^FD{self.model.ean}^FS^FO{config['LABEL_WIDTH_ROLLER_N']},150"
                f"^GB300,3,3^FS^FX Second section with recipient address and permit information."
                f"^CFA,14^FO{config['LABEL_WIDTH_ROLLER_N']},170^FD{self.model.label1}^FS^FO{config['LABEL_WIDTH_ROLLER_N']},190^FD{self.model.label8}^FS"
                f"^FS^FO{config['LABEL_WIDTH_ROLLER_N']},210^FD{self.model.label2}^FS"
                f"^FO{config['LABEL_WIDTH_ROLLER_N']},230^FD{self.model.label3}^FS^FO{config['LABEL_WIDTH_ROLLER_N']},250^FDMts: {self.model.label4}^FS"
                f"^FS^FO{config['LABEL_WIDTH_ROLLER_N']},270^FD{build_date()}  {self.model.label6}^FS^XZ")
        return code

    def build_eliot_code(self):
        code = f"^XA^FXinformation.^CFA,14"
        code += f"^FO{config['LABEL_WIDTH_ROLLER_E']},10^FD{build_date_eliot()} {self.model.label2}{self.model.label3}^FS"
        code += f"^FO480,10^FD{self.model.label2}^FS"
        code += f"^FO630,10^FD{self.model.ean}^FS"
        code += f"^FO{config['LABEL_WIDTH_ROLLER_E']},35^FDCOLOR: {self.model.label3} OC:{self.model.oc}^FS"
        code += f"^FO680,35^FD{self.model.label4}.00 MTS^FS"
        code += f"^CI28^FXbar code."
        code += f"^BY2,3,100^FO{config['LABEL_WIDTH_ROLLER_E_B']},60^BC^FD1{self.model.ean}3{build_eliot_barcode(self.model.label4)}.000:    ^FS^XZ"
        return code
