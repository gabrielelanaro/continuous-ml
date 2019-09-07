from contml import Resource, Version
from random import Random
import string


def test_resource():
    class RandomResource(Resource):
        def __init__(self, seed=42):
            self._rng = Random(seed)

        def check(self) -> Version:
            version = self._rng.choices(string.ascii_letters)
            return Version(version)

    r = RandomResource()
    assert isinstance(str, r.check().ref)
