class ZplModel:

    id_barcode: str
    label1: str
    label2: str
    label3: str
    label4: str
    label5: str
    label6: str
    label7: str
    label8: str
    ean: str
    oc: str

    def __init__(self, id_barcode: str, label1: str, label2: str, label3: str, label4: str, label5: str, label6: str, label7: str, label8: str, label9: str, oc: str):
        self.id_barcode = id_barcode
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.label6 = label6
        self.label7 = label7
        self.label8 = label8
        self.ean = label9
        self.oc = oc
