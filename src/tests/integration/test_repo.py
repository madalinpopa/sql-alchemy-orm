# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
from ormapp.adapters.repository import SqlRepository
from ormapp.domain import model


def test_repo_can_add_user(sqlite_session_factory):
    """
    Test repository can add a user.
    """

    session = sqlite_session_factory()
    repo = SqlRepository(session)
    user = model.User("1", "john", "secret")
    repo.add(user)
    session.commit()

    rows = list(session.execute("SELECT reference, username FROM users"))
    assert [("1", "john")] == rows


def test_repo_can_get_a_user(sqlite_session_factory):
    """
    Test repository can get an user from database.
    """
    session = sqlite_session_factory()
    session.execute(
        "INSERT INTO users (reference, version, username, password) VALUES "
        "('2', '1', 'steve', 'secret')"
    )

    repo = SqlRepository(session)
    user = repo.get("2")
    assert "2" == user.reference
    assert "steve" == user.username


def test_add_user_role(sqlite_session_factory):
    """
    Test if the role is saved when added an user.
    """
    session = sqlite_session_factory()
    repo = SqlRepository(session)
    user = model.User("1", "steve", "secret")
    user.role = model.Role("admin")
    repo.add(user)
    session.commit()

    rows = list(session.execute("SELECT name from roles"))
    assert [("admin",)] == rows
