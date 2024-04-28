from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAnswerRequest(_message.Message):
    __slots__ = ("question", "category")
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    question: str
    category: int
    def __init__(self, question: _Optional[str] = ..., category: _Optional[int] = ...) -> None: ...

class GetAnswerResponse(_message.Message):
    __slots__ = ("answer", "probability", "answer_id")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_ID_FIELD_NUMBER: _ClassVar[int]
    answer: str
    probability: float
    answer_id: int
    def __init__(self, answer: _Optional[str] = ..., probability: _Optional[float] = ..., answer_id: _Optional[int] = ...) -> None: ...
