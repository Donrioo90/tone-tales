from app import create_app, db
from app.models import User, Exercise, Nutrition
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="john_michael", email="johnbmichael@gmail.com", password_hash=generate_password_hash("password123"))
    user2 = User(username="wotto_smith", email="wotto@gmail.com", password_hash=generate_password_hash("password456"))

    exercise1 = Exercise(title="Morning Yoga", description="A calming yoga session.", image_url="https://via.placeholder.com/150")
    exercise2 = Exercise(title="HIIT Workout", description="High-intensity interval training.", image_url="https://via.placeholder.com/150")

    nutrition1 = Nutrition(title="Healthy Breakfast", content="Start your day with nutritious meals.")
    nutrition2 = Nutrition(title="Hydration Tips", content="Drink enough water for better health.")

    db.session.add_all([user1, user2, exercise1, exercise2, nutrition1, nutrition2])
    db.session.commit()

    print("Database seeded!")
