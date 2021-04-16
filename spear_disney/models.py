from flask_sqlalchemy import SQLAlchemy
from flask import current_app as spear_disney

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
