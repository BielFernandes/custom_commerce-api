from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import *

class Address(Base):
     __tablename__ = "address"

     id: Mapped[int] = mapped_column(primary_key=True)
     email_address: Mapped[str]
    #  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    #  user: Mapped["User"] = relationship(back_populates="addresses")

    #  def __repr__(self) -> str:
    #      return f"Address(id={self.id!r}, email_address={self.email_address!r})"