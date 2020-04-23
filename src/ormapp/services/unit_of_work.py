# coding: utf-8

# Author: Madalin Popa
# Date: joi, aprilie 2020
import abc

from ormapp.adapters.repository import Repository, SqlRepository


class UnitOfWork(abc.ABC):
    """
    Abstract unit of work.
    """
    repo: Repository = Repository

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    def collect_new_events(self):
        pass


class SqlUnitOfWork(UnitOfWork):
    """
    Concret unit of work class.
    """
    def __init__(self, session = None):
        self.session = session

    def __enter__(self) -> "SqlUnitOfWork":
        self.repo = SqlRepository(self.session)
        return super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()