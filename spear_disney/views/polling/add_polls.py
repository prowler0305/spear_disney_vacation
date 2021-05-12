from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for

from spear_disney.common.common import Common
from spear_disney.decorators import templated
from spear_disney.forms import AddQuestionForm
from spear_disney.models import PollQuestion, PollChoices, db


class AddPoll(MethodView):
    """

    """

    def __init__(self):
        self.add_poll_form = AddQuestionForm()
        self.disney_template_render_dict = dict(add_poll_form=self.add_poll_form)

    @templated()
    def get(self):
        """

        :return:
        """
        return self.disney_template_render_dict

    @templated()
    def post(self):
        """

        :return:
        """
        if self.add_poll_form.validate_on_submit():
            existing_poll = PollQuestion.query.filter_by(question_text=self.add_poll_form.question.data).one_or_none()
            if existing_poll is None:
                new_poll = PollQuestion(question_text=self.add_poll_form.question.data)
                db.session.add(new_poll)
                db.session.commit()
                new_poll_choices = PollChoices(question_id=new_poll.id, choices_text=self.add_poll_form.choices.data.split(","))
                db.session.add(new_poll_choices)
                db.session.commit()
            else:
                Common.create_flash_message("This Question already exists.", category_request=("add_poll", "danger"))
            return redirect(url_for("add_poll"))

        return self.disney_template_render_dict
