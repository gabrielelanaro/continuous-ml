from typing import Dict, Optional


class Version:
    """Dumb class to store a version string and associated metadata."""

    ref: str
    meta: Dict

    def __init__(self, ref, meta: Optional[Dict] = None):
        self.ref = ref
        self.meta = {} if meta is None else meta

    def __repr__(self):
        return f"Version({self.ref}, {self.meta})"
