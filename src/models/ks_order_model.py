from src.models.zpl_model import ZplModel


class KsOrderModel(ZplModel):

    def __init__(self, order_detail_id: str, client_name: str, ref: str, color: str, mts: str, kg: str, person: str):
        super().__init__(order_detail_id, client_name, ref, color, mts, kg, person)
