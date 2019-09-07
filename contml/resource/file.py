import os.path
import datetime

from .base import Resource
from ..version import Version


class LocalFileResource(Resource):
    path: str

    def __init__(self, path: str):
        """A simple local file resource.

        Changes in this resource are detected by monitoring its timestamp. New versions correspond
        to new timestamps.
        """
        self.path = path

    def check(self) -> Version:
        if not os.path.exists(self.path):
            ref = ""
        else:
            dtime = datetime.datetime.fromtimestamp(os.path.getmtime(self.path))
            ref = dtime.isoformat()

        return Version(ref, {"timestamp": ref, "exists": ref != "", "path": self.path})

    def __repr__(self):
        return f"LocalFileResource({self.path})"
