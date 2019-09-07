import abc

from typing import Hashable

from ..version import Version


class Resource(abc.ABC):
    @abc.abstractmethod
    def check(self) -> Version:
        """Check the current version of the resource"""

    @abc.abstractmethod
    def id(self) -> Hashable:
        """An immutable object that can be used to identify the resource"""

    def __id(self):
        return (self.__class__.__name__, self.id())

    def __eq__(self, other):
        return self.__id() == other.__id()

    def __hash__(self):
        return self.__id()
