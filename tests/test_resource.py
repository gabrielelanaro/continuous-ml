from contml import Resource, Version
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
