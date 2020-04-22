# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020


def test_user_entity_instance():
    """
    Test if user is instance of Entity
    """
    user = model.User("123", "john", "secret")
    assert isinstance(user, model.Entity)


def test_user_attributes():
    """
    Test user attributes
    """
    user = model.User("1", "john", "secret")
    assert hasattr(user, "reference")
    assert hasattr(user, "username")
    assert hasattr(user, "password")


def test_user_version_increment_wehn_update():
    """
    Test if version increments when update attributes
    """
    user = model.User("1", "john", "secret")
    user.username = "steve"
    assert 1 == user.version
