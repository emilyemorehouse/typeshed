# Stubs for gc

# NOTE: These are incomplete!

import typing

def collect(generation: int = -1) -> int: ...
def disable() -> None: ...
def enable() -> None: ...
def isenabled() -> bool: ...