from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import db, User, Exercise, Nutrition

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "Welcome to Tone Tales API!"})

@api.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@api.route("/exercises", methods=["GET"])
@jwt_required()
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([{"id": e.id, "title": e.title, "description": e.description, "image_url": e.image_url} for e in exercises])

@api.route("/nutrition", methods=["GET"])
@jwt_required()
def get_nutrition():
    nutrition = Nutrition.query.all()
    return jsonify([{"id": n.id, "title": n.title, "content": n.content} for n in nutrition])
