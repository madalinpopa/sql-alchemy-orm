# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020

from ormapp.domain import model


def test_orm_can_load_lines(sqlite_session_factory):
    """
    Test if orm maps correctly the entity.
    """
    session = sqlite_session_factory()
    session.execute(
        "INSERT INTO users (reference, version, username, password) VALUES "
        "('1', '1', 'steve', 'secret')"
    )
    expected = [model.User("1", "steve", "secret")]
    assert expected == session.query(model.User).all()


def test_orm_mapper_can_save_a_user(sqlite_session_factory):
    """
    Test if orm mappers can save an user in database.
    """
    session = sqlite_session_factory()
    user = model.User(reference="1", username="john", password="secret")
    session.add(user)
    session.commit()

    rows = list(session.execute("SELECT username, password from users"))
    assert [("john", "secret")] == rows


def test_orm_mapper_can_load_role(sqlite_session_factory):
    """
    Test if orm can load a role entity.
    """
    session = sqlite_session_factory()
    session.execute(
        "INSERT INTO roles (name) VALUES"
        "('vendor')"
    )
    expected = [model.Role("vendor")]
    assert expected == session.query(model.Role).all()


def test_orm_can_save_a_role(sqlite_session_factory):
    """
    Test if orm can save a role from entity.
    """
    session = sqlite_session_factory()
    role = model.Role("vendor")
    session.add(role)
    session.commit()

    rows = list(session.execute("SELECT name from roles"))
    assert [("vendor",)] == rows
