# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers, sessionmaker

from ormapp.adapters import database, orm


@pytest.fixture(scope="session")
def init_db_fixture():
    engine = create_engine("sqlite:///:memory:")
    database.metadata.create_all(engine)
    orm.start_mappers()
    yield engine
    clear_mappers()


@pytest.fixture(scope="function")
def sqlite_session_factory(init_db_fixture):
    session = sessionmaker(bind=init_db_fixture)
    yield session
    session().close()
    for table in reversed(database.metadata.sorted_tables):
        session().execute(table.delete())


