from typing import Any, Dict, Optional

JSONDict = Dict[str, Any]


class Version:
    """Dumb class to store a version string and associated metadata."""

    ref: str
    meta: JSONDict

    def __init__(self, ref: str, meta: Optional[JSONDict] = None):
        self.ref = ref
        self.meta = {} if meta is None else meta

    def __repr__(self):
        return f"Version({self.ref}, {self.meta})"
