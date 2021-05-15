from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for

from spear_disney.common.common import Common
from spear_disney.decorators import templated
from spear_disney.forms import AddQuestionForm, DisplayQuestions
from spear_disney.models import PollQuestion, PollChoices, db


class AddPoll(MethodView):
    """

    """

    def __init__(self):
        self.add_poll_form = AddQuestionForm()
        self.delete_poll_form = DisplayQuestions()
        self.disney_template_render_dict = dict(add_poll_form=self.add_poll_form, delete_poll_form=self.delete_poll_form)

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
        if self.delete_poll_form.delete.data:
            self.delete()
        else:
            if self.add_poll_form.validate_on_submit():
                existing_poll = PollQuestion.query.filter_by(question_text=self.add_poll_form.question.data).one_or_none()
                if existing_poll is None:
                    new_poll = PollQuestion(question_text=self.add_poll_form.question.data)
                    db.session.add(new_poll)
                    db.session.commit()
                    new_poll_choices = PollChoices(question_id=new_poll.id, choices_text=self.add_poll_form.choices.data.split(","))
                    db.session.add(new_poll_choices)
                    db.session.commit()
                    Common.create_flash_message("Poll Question added successfully",
                                                category_request=("add_poll", "success"))
                else:
                    Common.create_flash_message("This Question already exists.",
                                                category_request=("add_poll", "danger"))
                return redirect(url_for("add_poll"))

        return self.disney_template_render_dict

    def delete(self):
        """
        Delete a Poll Question based on its id
        :return:
        """
        if self.delete_poll_form.validate_on_submit():
            delete_question = PollQuestion.query.get(self.delete_poll_form.display_question.data.id)
            if delete_question is not None:
                db.session.delete(delete_question)
                db.session.commit()
                Common.create_flash_message("Existing Poll Question deleted successfully",
                                            category_request=("delete_poll", "success"))
                self.disney_template_render_dict["delete_poll_form"] = DisplayQuestions()
                redirect(url_for("add_poll"))
            else:
                Common.create_flash_message("Error has occurred", category_request=("delete_poll", "danger"))

        return self.disney_template_render_dict
