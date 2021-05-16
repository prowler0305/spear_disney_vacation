from flask_sqlalchemy import SQLAlchemy
from flask import current_app as spear_disney
from sqlalchemy.dialects.postgresql import ARRAY

db = SQLAlchemy()


class Suggestions(db.Model):
    """

    """
    __tablename__ = 'suggestions'

    id = db.Column(db.Integer, primary_key=True)
    by_who = db.Column(db.String(20), nullable=False)
    suggestion = db.Column(db.String(100), nullable=False)
    suggestion_category = db.Column(db.String(50))

    def __init__(self, by_who, suggestion, suggestion_category):
        """

        :param by_who:
        :param suggestion:
        ":param suggestion_category
        """
        self.by_who = by_who
        self.suggestion = suggestion
        self.suggestion_category = suggestion_category


class PollQuestion(db.Model):
    """

    """
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String, nullable=False)
    choices = db.relationship("PollChoices", backref="poll_question", lazy=True, uselist=False, cascade="delete")

    def __init__(self, question_text):
        self.question_text = question_text

    def __str__(self):
        return self.question_text


class PollChoices(db.Model):
    """

    """
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("poll_question.id"), nullable=False)
    # choices_text = db.Column(db.ARRAY(db.String))
    choices_text = db.Column(db.String)
    choices_results = db.Column(db.String)

    def __init__(self, question_id, choices_text, choices_results=None):
        self.choices_results = choices_results
        self.question_id = question_id
        self.choices_text = choices_text
