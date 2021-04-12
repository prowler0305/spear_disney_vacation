from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ChristianSuggestion(FlaskForm):
    suggestion = StringField("Suggestion", validators=[DataRequired()])
    submit = SubmitField("Submit")
