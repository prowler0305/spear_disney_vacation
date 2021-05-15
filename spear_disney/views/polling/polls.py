from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for
from spear_disney.decorators import templated
from spear_disney.forms import Suggestion, PollForm
from spear_disney.models import Suggestions, db, PollQuestion


class Polls(MethodView):
    """

    """
    def __init__(self):
        # self.question_poll = PollForm("What tastes better, beignets or bao bun?", question_choices=[("", ""), ('beignets', 'beignets'), ('bao_bun', 'bao bun')])
        self.disney_template_render_dict = dict()

    @templated()
    def get(self):
        poll_question_list = PollQuestion.query.all()
        poll_form_list = list()
        for poll_question in poll_question_list:
            choices_list = [("", "")]
            for choice in poll_question.choices.choices_text:
                temp_tuple = (choice, choice)
                choices_list.append(temp_tuple)
            poll_form_list.append(PollForm(poll_question.question_text, question_choices=choices_list))
        self.disney_template_render_dict["poll_forms"] = poll_form_list
        return self.disney_template_render_dict

    # @templated()
    # def post(self):
    #     if self.suggest_form.submit.data:
    #         new_suggestion = Suggestions(self.suggest_form.by_who.data, self.suggest_form.suggestion.data,
    #                                      self.suggest_form.suggestion_category.data)
    #         db.session.add(new_suggestion)
    #     elif self.suggest_form.delete_entry.data:
    #         entry_to_delete = Suggestions.query.get(self.suggest_form.delete_id.data)
    #         db.session.delete(entry_to_delete)
    #
    #     db.session.commit()
    #
    #     return redirect(url_for("polls"))
