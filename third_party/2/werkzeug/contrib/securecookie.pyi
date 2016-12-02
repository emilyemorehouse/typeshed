# Stubs for werkzeug.contrib.securecookie (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from hmac import new as hmac
from hashlib import sha1 as _default_hash
from werkzeug.contrib.sessions import ModificationTrackingDict

class UnquoteError(Exception): ...

class SecureCookie(ModificationTrackingDict):
    hash_method = ...  # type: Any
    serialization_method = ...  # type: Any
    quote_base64 = ...  # type: Any
    secret_key = ...  # type: Any
    new = ...  # type: Any
    def __init__(self, data=None, secret_key=None, new=True): ...
    @property
    def should_save(self): ...
    @classmethod
    def quote(cls, value): ...
    @classmethod
    def unquote(cls, value): ...
    def serialize(self, expires=None): ...
    @classmethod
    def unserialize(cls, string, secret_key): ...
    @classmethod
    def load_cookie(cls, request, key='', secret_key=None): ...
    def save_cookie(self, response, key='', expires=None, session_expires=None, max_age=None, path='', domain=None, secure=None, httponly=False, force=False): ...