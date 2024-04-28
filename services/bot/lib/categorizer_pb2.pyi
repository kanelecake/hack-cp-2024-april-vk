from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetCategoryRequest(_message.Message):
    __slots__ = ("question",)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: str
    def __init__(self, question: _Optional[str] = ...) -> None: ...

class GetCategoryResponse(_message.Message):
    __slots__ = ("category", "probability")
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    category: int
    probability: float
    def __init__(self, category: _Optional[int] = ..., probability: _Optional[float] = ...) -> None: ...
