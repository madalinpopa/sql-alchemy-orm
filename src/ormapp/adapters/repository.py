# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
import abc

from ormapp.domain.model import User


class Repository(abc.ABC):
    """
    Abstract repository.
    """

    def __init__(self) -> None:
        self.seen = set()

    def add(self, user) -> None:
        self._add(user)
        self.seen.add(user)

    def get(self, reference) -> User:
        user = self._get(reference)
        if user:
            self.seen.add(user)
        return user

    @abc.abstractmethod
    def _add(self, user) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, reference) -> User:
        raise NotImplementedError


class SqlRepository(Repository):

    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, user) -> None:
        self.session.add(user)

    def _get(self, reference) -> User:
        return (
            self.session.query(User).filter_by(reference=reference).one_or_none()
        )
