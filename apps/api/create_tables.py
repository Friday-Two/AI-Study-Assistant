from app.core.database import engine
from app.db.base import Base

# Import models so SQLAlchemy registers them
from app.models import User  # noqa: F401

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")