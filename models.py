from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.sql import func

from database import Base


# =====================================================
# BRANCH TABLE
# =====================================================

class Branch(Base):

    __tablename__ = "branches"

    branch_id = Column(Integer, primary_key=True, autoincrement=True)

    branch_name = Column(String(200), unique=True, nullable=False)

    city = Column(String(100))

    manager_name = Column(String(150))

    created_at = Column(DateTime, server_default=func.now())


# =====================================================
# CUSTOMER TABLE
# =====================================================

class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)

    customer_id_code = Column(String(50))

    customer_name = Column(String(200), nullable=False)

    account_number = Column(String(30), unique=True, nullable=False)

    password = Column(String(100), nullable=False)

    account_type = Column(String(100))

    branch = Column(String(200))

    ifsc = Column(String(30))

    currency = Column(String(20))

    city = Column(String(100))

    opening_balance = Column(Float)

    total_credits = Column(Float)

    total_debits = Column(Float)

    closing_balance = Column(Float)

    total_transactions = Column(Integer)

    statement_start = Column(Date)

    statement_end = Column(Date)

    created_at = Column(DateTime, server_default=func.now())


# =====================================================
# TRANSACTION TABLE
# =====================================================

class Transaction(Base):

    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)

    account_number = Column(
        String(30),
        ForeignKey("customers.account_number"),
        nullable=False
    )

    transaction_date = Column(Date)

    description = Column(Text)

    reference = Column(String(100))

    transaction_type = Column(String(10))

    debit = Column(Float)

    credit = Column(Float)

    balance = Column(Float)


# =====================================================
# ADMIN TABLE
# =====================================================

class Admin(Base):

    __tablename__ = "admins"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)

    admin_name = Column(String(150), nullable=False)

    username = Column(String(100), unique=True, nullable=False)

    password = Column(String(100), nullable=False)

    branch = Column(String(200))


# =====================================================
# BRANCH MANAGER TABLE
# =====================================================

class Manager(Base):

    __tablename__ = "managers"

    manager_id = Column(Integer, primary_key=True, autoincrement=True)

    manager_name = Column(String(150), nullable=False)

    username = Column(String(100), unique=True, nullable=False)

    password = Column(String(100), nullable=False)

    branch = Column(String(200))