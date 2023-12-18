from app.db.postgres.connector import PostgresqlManager
from sqlalchemy import Column, DateTime, Index, Integer, String, Boolean
from datetime import datetime


class ChangesTracking(PostgresqlManager.Base):
    __abstract__ = True

    created_on = Column(DateTime(), default=datetime.utcnow)
    updated_on = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


class User(ChangesTracking):
    __tablename__ = 'users'

    id  = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class ElementsToProcess(ChangesTracking):
    __tablename__ = 'elementstoprocess'

    id  = Column(Integer, primary_key=True, index=True)
    id_bulk = Column(Integer, nullable=False)
    retries = Column(Integer, default=None)
    status= Column(Integer, nullable=False)
    name = Column(String, nullable=False)


    __table_args__ = (
        Index('ElementsToProcess_idBulk_IDX',  'id_bulk', 'status'),
        Index('ElementsToProcess_status_IDX', 'status'),
    )

