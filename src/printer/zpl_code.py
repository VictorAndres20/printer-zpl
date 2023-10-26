from src.models.zpl_model import ZplModel


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
