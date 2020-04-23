# coding: utf-8

# Author: Madalin Popa
# Date: joi, aprilie 2020
from ormapp.domain import model
from ormapp.services.unit_of_work import SqlUnitOfWork


def test_uow_can_add_an_user(sqlite_session_factory):
    """
    Test if unit of work can add a new user.
    """
    session = sqlite_session_factory()
    uow = SqlUnitOfWork(session)
    user = model.User(reference="1", username="john", password="secret")
    with uow:
        uow.repo.add(user)
        uow.commit()

    row = list(session.execute("SELECT reference, username, password FROM users"))
    expected = [("1", "john", "secret")]
    assert expected == row


def test_uow_can_get_an_user(sqlite_session_factory):
    """
    Test to see if uow can get an user by reference.
    """
    session = sqlite_session_factory()

    session.execute(
        "INSERT INTO users (reference, version, username, password) VALUES"
        "('1', 1, 'steve', 'secret')"
    )

    uow = SqlUnitOfWork(session)
    with uow:
        user = uow.repo.get("1")
        assert user is not None
        assert "steve" == user.username


def test_uow_role_saved_along_with_user(sqlite_session_factory):
    """
    Test if the role is saved along with the user.
    """
    session = sqlite_session_factory()
    uow = SqlUnitOfWork(session)
    user = model.User("1", "steve", "secret")
    user.role = model.Role("admin")

    with uow:
        uow.repo.add(user)
        uow.commit()

    rows = list(session.execute("SELECT name FROM roles"))
    expected = [('admin',)]
    assert expected == rows