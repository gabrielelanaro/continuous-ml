from contml import Resource, Version
from contml.resource.file import LocalFileResource

from random import Random
import string


def test_resource():
    class RandomResource(Resource):
        def __init__(self, seed=42):
            self._rng = Random(seed)

        def check(self) -> Version:
            ref = "".join(self._rng.choices(string.ascii_letters, k=16))
            return Version(ref)

    r = RandomResource()
    assert isinstance(r.check().ref, str)


def test_local_file_resource(tmp_path):
    p = tmp_path / "test.txt"

    r = LocalFileResource(str(p))

    # Non existent at first
    assert r.check().ref == ""

    # Once it exists we do timestamp
    p.write_text("Hello")
    assert r.check().ref != ""
