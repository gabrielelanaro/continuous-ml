import abc
from .version import Version


class Resource(abc.ABC):
    @abc.abstractmethod
    def check(self) -> Version:
        """Check the current version of the resource"""
