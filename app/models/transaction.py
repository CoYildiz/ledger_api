from decimal import Decimal
from datetime import datetime

from app.models.account import Account
from sqlalchemy import ForeignKey , Numeric, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Transaction(Base):
    __tablename__  = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("account.id", ondelete="RESTRICT")) # for referential action its important
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=12, scale=2))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    # relationship
    account: Mapped["Account"] = relationship(back_populates="transactions")
