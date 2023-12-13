"""KSOrderModel"""
from src.models.zpl_model import ZplModel

class KsOrderEanModel(ZplModel):

    def __init__(self, order_detail_id: str, client_name: str, ref: str, color: str, mts: str, kg: str, person: str, client_cod: str, ref_description: str, ean: str, oc: str):
        """KSOrderModel"""
        super().__init__(order_detail_id, client_name, ref, color, mts, kg, person, client_cod, ref_description, ean, oc)