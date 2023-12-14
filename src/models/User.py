from typing import List
from typing import Optional
from sqlalchemy import String, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import *

class User(Base):
     __tablename__ = "user"
     id: Mapped[int] = mapped_column(primary_key=True)
     fname: Mapped[str] = mapped_column(String(30), nullable=False)
     lname: Mapped[str] = mapped_column(String(30), nullable=False)
     email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
     password: Mapped[str] = mapped_column(String, nullable=False)
     admin: Mapped[bool] = mapped_column(Boolean, default=False)
     created_at: Mapped[str] = mapped_column(Date)

    #  def __repr__(self) -> str:
    #      return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"