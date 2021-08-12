"""Wrapper for Notion User objects."""

import logging

from .core import NestedObject, TypedObject

log = logging.getLogger(__name__)


class User(TypedObject):
    """Represents a User in Notion."""

    object: str = "user"
    id: str = None
    name: str = None
    avatar_url: str = None


class Person(User, type="person"):
    """Represents a Person in Notion."""

    class NestedPerson(NestedObject):
        email: str

    person: NestedPerson = None

    def __getitem__(self, key):
        return self.person[key]


class Bot(User, type="bot"):
    """Represents a Bot in Notion."""

    class NestedBot(NestedObject):
        pass

    bot: NestedBot = None

    def __getitem__(self, key):
        return self.bot[key]