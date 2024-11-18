from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class State(Base):
    __tablename__ = 'states'
    __table_args__ = (PrimaryKeyConstraint('id', name='states_pkey'),)

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,primary_key=True,autoincrement=True,nullable=False)
    statename: Mapped[String] = mapped_column('state_name',String(255),nullable=True)
    countries_id:Mapped[BigInteger] = mapped_column('countries_id',BigInteger,ForeignKey('countries.id'),nullable=True)
    status:Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at:Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at:Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)