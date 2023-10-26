from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Response(BaseModel, Generic[T]):
    ok: bool = True
    error: str = ''
    message: str = ''
    data: Optional[T] = None
