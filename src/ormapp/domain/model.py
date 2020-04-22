# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
import abc

from sqlalchemy.ext.hybrid import hybrid_property


class Role:
    """
    Role value object
    """

    def __init__(self, name):
        self._name = name
        self._user = None

    def __repr__(self):
        return self._name

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Role):
            raise ValueError("Not instance of Role")
        return self._name == o._name

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        return Role(value)


class Entity(abc.ABC):
    """
    Entity class.
    """

    def __init__(self, reference):
        self._reference = reference
        self._version = 0

    @hybrid_property
    def reference(self):
        return self._reference

    @hybrid_property
    def version(self):
        return self._version

    def increment_version(self):
        self._version += 1


class User(Entity):
    """
    User entity.
    """

    def __init__(self, reference, username, password):
        super().__init__(reference)
        self._password = password
        self._username = username
        self._reference = reference
        self._role = None

    @hybrid_property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
        self.increment_version()

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        self.increment_version()

    @hybrid_property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        self.increment_version()

    @hybrid_property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = valuemake
        self.increment_version()
