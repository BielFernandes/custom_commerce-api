from typing import List
from typing import Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import *

class User(Base):
     __tablename__ = "user"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     fullname: Mapped[Optional[str]]
     addresses: Mapped[List["Address"]] = relationship(
         back_populates="user", cascade="all, delete-orphan"
     )

     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"