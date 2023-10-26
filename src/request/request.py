from pydantic import BaseModel


class OrderDetailRequest(BaseModel):
    detail_id: str
    client_name: str
    ref: str
    color: str
    mts: str
    kg: str
    person: str
