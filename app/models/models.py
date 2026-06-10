from datetime import datetime
from typing import Optional
from sqlalchemy import BigInteger, String, Float, Integer, Text, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum

class Base(DeclarativeBase):
    pass

class OrderStatus(str, enum.Enum):
    PENDING = "🟡 Kutilmoqda"
    IN_PROGRESS = "🔵 Jarayonda"
    DONE = "🟢 Tayyor"
    CANCELED = "🔴 Bekor qilingan"

class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class TariffEnum(str, enum.Enum):
    BASIC = "🥉 BASIC"
    PREMIUM = "🥈 PREMIUM"
    VIP = "🥇 VIP"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    fullname: Mapped[str] = mapped_column(String(255))
    username: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    tariff: Mapped[str] = mapped_column(SQLEnum(TariffEnum), default=TariffEnum.BASIC)
    requests_left: Mapped[int] = mapped_column(Integer, default=10) # 10 defaults
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    orders = relationship("Order", back_populates="user")
    payments = relationship("Payment", back_populates="user")

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    service: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    file_url: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(SQLEnum(OrderStatus), default=OrderStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    
    user = relationship("User", back_populates="orders")

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[int] = mapped_column(Integer)
    receipt_photo: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(SQLEnum(PaymentStatus), default=PaymentStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user = relationship("User", back_populates="payments")

class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
