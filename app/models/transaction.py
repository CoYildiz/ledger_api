from decimal import Decimal
from datetime import datetime

from app.models.account import Account
from sqlalchemy import ForeignKey , Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Transaction(Base):
    __tablename__  = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=2))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    # relationship
    account: Mapped["Account"] = relationship(back_populates="transactions")
