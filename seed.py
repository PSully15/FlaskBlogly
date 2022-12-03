from models import User, db
from app import app

db.drop_all()
db.create_all()

# Users
user1 = User(
    first_name="John",
    last_name="Doe"
)

db.session.add(user1)

db.session.commit()