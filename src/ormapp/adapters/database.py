# coding: utf-8

# Author: Madalin Popa
# Date: miercuri, aprilie 2020

# Metadata
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# metadata
metadata = MetaData()

# engine
engine = create_engine("sqlite:///:memory:")

# session
session = scoped_session(sessionmaker(bind=engine))


# init db
def init_db():
    metadata.create_all(bind=engine)
