from typing import Generic, Optional, TypeVar, Any
from pydantic import BaseModel

DataType = TypeVar("DataType")


class BaseResponse(BaseModel, Generic[DataType]):
    success: bool = True
    data: Optional[DataType] = None
    message: Optional[str] = None


class ErrorDetails(BaseModel):
    code: str
    message: str
    details: Optional[Any] = None
    request_id: Optional[str] = None


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetails
