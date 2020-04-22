# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import mapper, relationship

from ormapp.adapters.database import metadata
from ormapp.domain import model

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(32), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id"))
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(32), nullable=False),
    Column("version", String(32), nullable=False),
    Column("username", String(32), nullable=False),
    Column("password", String(32), nullable=False),
)


def start_mappers():
    """
    Start the mapping of entities with the tables.
    """
    roles_mapper = mapper(
        model.Role,
        roles,
        properties={
            "_name": roles.c.name,
            "_user": relationship(model.User, back_populates="_role")
        }
    )
    mapper(
        model.User,
        users,
        version_id_col=users.c.version,
        version_id_generator=False,
        properties={
            "_reference": users.c.reference,
            "_version": users.c.version,
            "_username": users.c.username,
            "_password": users.c.password,
            "_role": relationship(roles_mapper, back_populates="_user", uselist=False)
        }
    )
