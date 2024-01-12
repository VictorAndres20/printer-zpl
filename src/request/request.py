from typing import Any, Optional

from pydantic import BaseModel


class OrderDetailRequest(BaseModel):
    ip: str
    printer: int
    detail_id: str
    client_name: str
    ref: str
    color: str
    mts: str | int
    kg: str
    person: Optional[str]


class RolerRequest(BaseModel):
    ip: str
    printer: int
    detail_id: Optional[str]
    desc: str
    ref: str
    color: str
    mts: str | int
    person: Optional[str]

class OrderDetailEanRequest(BaseModel):
    ip: str
    printer: int
    detail_id: str
    client_name: str
    ref: str
    color: str
    mts: str | int
    kg: str
    person: Optional[str]
    client_cod: str
    ref_description: str
    ean: str
    oc: str
