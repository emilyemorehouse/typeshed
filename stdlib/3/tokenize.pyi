from typing import Any, Callable, Generator, Iterable, List, NamedTuple, Optional, Union, Sequence, TextIO, Tuple
from builtins import open as _builtin_open
from token import *  # noqa: F403

COMMENT = ...  # type: int
NL = ...  # type: int
ENCODING = ...  # type: int

_Position = Tuple[int, int]

_TokenInfo = NamedTuple('TokenInfo', [
    ('type', int),
    ('string', str),
    ('start', _Position),
    ('end', _Position),
    ('line', str)
])

class TokenInfo(_TokenInfo):
    @property
    def exact_type(self) -> int: ...

# Backwards compatible tokens can be sequences of a shorter length too
_Token = Union[TokenInfo, Sequence[Union[int, str, _Position]]]

class TokenError(Exception): ...
class StopTokenizing(Exception): ...

class Untokenizer:
    tokens = ...  # type: List[str]
    prev_row = ...  # type: int
    prev_col = ...  # type: int
    encoding = ...  # type: Optional[str]
    def __init__(self) -> None: ...
    def add_whitespace(self, start: _Position) -> None: ...
    def untokenize(self, iterable: Iterable[_Token]) -> str: ...
    def compat(self, token: Sequence[Union[int, str]], iterable: Iterable[_Token]) -> None: ...

def untokenize(iterable: Iterable[_Token]) -> Any: ...
def detect_encoding(readline: Callable[[], bytes]) -> Tuple[str, Sequence[bytes]]: ...
def tokenize(readline: Callable[[], bytes]) -> Generator[TokenInfo, None, None]: ...

def open(filename: Union[str, bytes, int]) -> TextIO: ...

# Names in __all__ with no definition:
#   AMPER
#   AMPEREQUAL
#   ASYNC
#   AT
#   ATEQUAL
#   AWAIT
#   CIRCUMFLEX
#   CIRCUMFLEXEQUAL
#   COLON
#   COMMA
#   DEDENT
#   DOT
#   DOUBLESLASH
#   DOUBLESLASHEQUAL
#   DOUBLESTAR
#   DOUBLESTAREQUAL
#   ELLIPSIS
#   ENDMARKER
#   EQEQUAL
#   EQUAL
#   ERRORTOKEN
#   GREATER
#   GREATEREQUAL
#   INDENT
#   ISEOF
#   ISNONTERMINAL
#   ISTERMINAL
#   LBRACE
#   LEFTSHIFT
#   LEFTSHIFTEQUAL
#   LESS
#   LESSEQUAL
#   LPAR
#   LSQB
#   MINEQUAL
#   MINUS
#   NAME
#   NEWLINE
#   NOTEQUAL
#   NT_OFFSET
#   NUMBER
#   N_TOKENS
#   OP
#   PERCENT
#   PERCENTEQUAL
#   PLUS
#   PLUSEQUAL
#   RARROW
#   RBRACE
#   RIGHTSHIFT
#   RIGHTSHIFTEQUAL
#   RPAR
#   RSQB
#   SEMI
#   SLASH
#   SLASHEQUAL
#   STAR
#   STAREQUAL
#   STRING
#   TILDE
#   VBAR
#   VBAREQUAL
#   tok_name
