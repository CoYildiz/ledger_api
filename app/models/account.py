from app.db.base import Base
from decimal import Decimal

from sqlalchemy import Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime


class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner_name: Mapped[str]
    balance: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=2))# might be numeric
    created_at: Mapped[datetime] = mapped_column(server_default= func.now())
    # relationship # it will change later because of many to many relationship
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="account")
