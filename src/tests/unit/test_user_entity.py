# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
from ormapp.domain import model


class TestUserEntity:

    def test_user_entity_instance(self):
        """
        Test if user is instance of Entity
        """
        user = model.User("123", "john", "secret")
        assert isinstance(user, model.Entity)

    def test_user_attributes(self):
        """
        Test user attributes
        """
        user = model.User("1", "john", "secret")
        assert hasattr(user, "reference")
        assert hasattr(user, "username")
        assert hasattr(user, "password")
        assert hasattr(user, "role")

    def test_user_version_increment_wehn_update(self):
        """
        Test if version increments when update attributes
        """
        user = model.User("1", "john", "secret")
        user.username = "steve"
        assert 1 == user.version

    def test_user_has_role_instance(self):
        """
        Test if user has a role instance
        """
        user = model.User("1", "john", "secret")
        user.role = model.Role("admin")
        assert isinstance(user.role, model.Role)


class TestRoleValueObject:
    """
    Test Role value object.
    """

    def test_role_value_object_has_attribute(self):
        """
        Test role attributes.
        """
        role = model.Role("admin")
        assert hasattr(role, "name")
        assert hasattr(role, "user")

    def test_role_equality(self):
        """
        Test two roles are equal if the name is the same.
        """
        role1 = model.Role("admin")
        role2 = model.Role("admin")
        assert role1 == role2

    def test_role_representation(self):
        """
        Test role representation.
        """
        role = model.Role("admin")
        assert "admin" == repr(role)