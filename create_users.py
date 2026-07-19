from database import get_session
from models import Admin, Manager, Branch


def create_default_users():
    session = get_session()

    try:
        # -------------------------------------------------
        # Create Default Branch
        # -------------------------------------------------
        branch = session.query(Branch).filter_by(
            branch_name="Coimbatore - Mettupalayam Road"
        ).first()

        if branch is None:
            branch = Branch(
                branch_name="Coimbatore - Mettupalayam Road",
                city="Coimbatore",
                manager_name="Coimbatore Manager"
            )
            session.add(branch)

        # -------------------------------------------------
        # Create Default Manager
        # -------------------------------------------------
        manager = session.query(Manager).filter_by(
            username="manager"
        ).first()

        if manager is None:
            manager = Manager(
                manager_name="Coimbatore Manager",
                username="manager",
                password="manager123",
                branch="Coimbatore - Mettupalayam Road"
            )
            session.add(manager)

        # -------------------------------------------------
        # Create Default Admin
        # -------------------------------------------------
        admin = session.query(Admin).filter_by(
            username="admin"
        ).first()

        if admin is None:
            admin = Admin(
                admin_name="Axis Admin",
                username="admin",
                password="admin123",
                branch="Head Office"
            )
            session.add(admin)

        session.commit()

        print("=" * 60)
        print("DEFAULT USERS CREATED SUCCESSFULLY")
        print("=" * 60)

        print("\nADMIN LOGIN")
        print("Username : admin")
        print("Password : admin123")

        print("\nMANAGER LOGIN")
        print("Username : manager")
        print("Password : manager123")

    except Exception as e:
        session.rollback()
        print("Error:", e)

    finally:
        session.close()


if __name__ == "__main__":
    create_default_users()