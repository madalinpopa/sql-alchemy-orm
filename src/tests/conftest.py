# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020

import pytest
from sqlalchemy.orm import clear_mappers

from ormapp.adapters import database, orm


@pytest.fixture()
def init_db_fixture():
    database.init_db()


@pytest.fixture
def sqlite_session_factory(init_db_fixture):
    orm.start_mappers()
    yield database.session
    database.session().close()
    clear_mappers()