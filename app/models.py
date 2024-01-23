from typing import List

from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    user_chat_id: Mapped[int] = mapped_column(Integer)
    user_first_name: Mapped[str] = mapped_column(String(50))
    user_last_name: Mapped[str] = mapped_column(String(50))
    user_username: Mapped[str] = mapped_column(String(50))


class Subject(Base):
    __tablename__ = "subject"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    user_chat_id: Mapped[int] = mapped_column(Integer)
    user_first_name: Mapped[str] = mapped_column(String(50))
    user_last_name: Mapped[str] = mapped_column(String(50))
    user_username: Mapped[str] = mapped_column(String(50))
    rules: Mapped[List["Rule"]] = relationship()


class Rule(Base):
    __tablename__ = "rule"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String)

class Rule_Subject(Base):
    __tablename__ = "rule_subject"

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id = mapped_column(ForeignKey("subject.id"))
    rule_id = mapped_column(ForeignKey("rule.id"))







