from app.db.postgres.connector import PostgresqlManager
from sqlalchemy import Column, DateTime, Index, Integer, String
from datetime import datetime


class ChangesTracking(PostgresqlManager.Base):
    __abstract__ = True

    created_on = Column(DateTime(), default=datetime.utcnow)
    updated_on = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


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

