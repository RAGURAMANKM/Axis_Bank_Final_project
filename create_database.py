from database import Base
from database import engine

# Import all models so SQLAlchemy knows about them
from models import (
    Customer,
    Transaction,
    Admin,
    Manager,
    Branch
)


def create_database():
    print("=" * 60)
    print("Creating PostgreSQL tables...")
    print("=" * 60)

    Base.metadata.create_all(bind=engine)

    print("=" * 60)
    print("Database created successfully!")
    print("=" * 60)


if __name__ == "__main__":
    create_database()