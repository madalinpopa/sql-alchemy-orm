# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
from ormapp.adapters.repository import Repository, SqlRepository


def test_repository_instace():
    """
    Test repository instance.
    """
    repo = SqlRepository(None)
    assert isinstance(repo, Repository)


def test_repository_attributes():
    """
    Test repository attribute
    """
    repo = SqlRepository(None)
    assert hasattr(repo, "seen")
    assert hasattr(repo, "session")
