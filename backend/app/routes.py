from flask import Blueprint, jsonify, request
from .models import db, User, Exercise, Nutrition

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Welcome to Tone Tales API!"})

@main.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([{"id": e.id, "title": e.title, "description": e.description, "image_url": e.image_url} for e in exercises])

@main.route("/nutrition", methods=["GET"])
def get_nutrition():
    nutrition = Nutrition.query.all()
    return jsonify([{"id": n.id, "title": n.title, "content": n.content} for n in nutrition])
