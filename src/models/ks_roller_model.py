from src.models.zpl_model import ZplModel


class KsRollerModel(ZplModel):

    def __init__(self, mts: str, ref: str, color: str, person: str, desc: str, order_detail_id: str):
        super().__init__(mts, ref, color, person, desc, order_detail_id, '', '', '', '', '')
