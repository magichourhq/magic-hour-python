from typing import (
    Union,
)
from typing_extensions import (
    Literal,
    TypeVar,
    override,
)

_T = TypeVar("_T")


class NotGiven:
    """
    Used to distinguish omitted keyword arguments from those passed explicitly
    with the value None.
    """

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


NotGivenOr = Union[_T, NotGiven]
NOT_GIVEN = NotGiven()
