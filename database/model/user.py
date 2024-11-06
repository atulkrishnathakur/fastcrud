from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pkey'),
        UniqueConstraint('email', name='uix_email')
    )

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,primary_key=True,autoincrement=True,nullable=False)
    firstname: Mapped[String] = mapped_column('first_name',String(255),nullable=False)
    secondname:Mapped[String] = mapped_column('second_name',String(255),nullable=True)
    email:Mapped[String] = mapped_column('email',String(255),unique=True,nullable=True)
    password:Mapped[String] = mapped_column('password',String(255),nullable=True)
    status:Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at:Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at:Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)