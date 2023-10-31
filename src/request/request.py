from typing import Optional

from pydantic import BaseModel


class OrderDetailRequest(BaseModel):
    detail_id: str
    client_name: str
    ref: str
    color: str
    mts: str | int
    kg: str
    person: Optional[str]


class RolerRequest(BaseModel):
    detail_id: Optional[str]
    desc: str
    ref: str
    color: str
    mts: str | int
    person: Optional[str]
