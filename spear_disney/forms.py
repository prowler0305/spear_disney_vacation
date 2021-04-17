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
