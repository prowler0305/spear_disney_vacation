from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, InputRequired


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
