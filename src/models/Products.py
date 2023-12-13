from sqlalchemy import String, Text, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column
from base_model import *

class Product(Base):
    __tablename__= "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    ean: Mapped[str] = mapped_column(String(13), unique=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(Date)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, ean={ean})"