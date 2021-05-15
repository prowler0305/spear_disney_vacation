from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, InputRequired

from spear_disney import db
from spear_disney.models import PollQuestion


class Suggestion(FlaskForm):
    delete_id = HiddenField("Hidden table row ID")
    by_who = SelectField("Who's Suggestion is this?",
                         choices=[("", ""),
                                  ('christian', 'Christian'),
                                  ('sarah', 'Sarah'),
                                  ("mom", "Mom"),
                                  ("dad", "Dad")],
                         default="", validators=[InputRequired()])
    suggestion_category = SelectField("Category",
                                      choices=[("", ""),
                                               ("rides_attractions", "Rides/Attractions"),
                                               ("dining", "Dining")],
                                      validators=[InputRequired()])
    suggestion = StringField("Suggestion", validators=[DataRequired()])
    submit = SubmitField("Submit")
    delete_entry = SubmitField("Delete")


class PollForm(FlaskForm):
    def __init__(self, label_text, question_choices, **kwargs):
        super(PollForm, self).__init__(**kwargs)
        self.question.label.text = label_text
        self.question.choices = question_choices

    question = SelectField(default="", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddQuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    choices = StringField("Choices", validators=[DataRequired()])
    add = SubmitField("Add")


def get_current_questions():
    return db.session.query(PollQuestion).all()


class DisplayQuestions(FlaskForm):
    # def __init__(self, display_question_text, **kwargs):
    #     super(DisplayQuestions, self).__init__(**kwargs)
    #     self.display_question = display_question_text

    # display_question = SelectField(validators=[DataRequired()])
    display_question = QuerySelectField("Existing Questions", validators=[DataRequired()],
                                        query_factory=get_current_questions, get_label="question_text")
    delete = SubmitField("Delete")
