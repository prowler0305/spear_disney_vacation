import json

from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for

from spear_disney.common.common import Common
from spear_disney.decorators import templated
from spear_disney.forms import Suggestion, PollForm
from spear_disney.models import Suggestions, db, PollQuestion, PollChoices


class Polls(MethodView):
    """

    """
    def __init__(self):
        self.disney_template_render_dict = dict()

    @templated()
    def get(self):
        poll_question_list = PollQuestion.query.all()
        poll_questions_list = list()
        for poll_question in poll_question_list:
            choices_list = [("", "")]
            for choice in poll_question.choices.choices_text.strip('"{}').replace('"', '').split(","):
                temp_tuple = (choice, choice)
                choices_list.append(temp_tuple)
            single_poll_question_tuple = (
                PollForm(poll_question.question_text, question_choices=choices_list, poll_question_id=poll_question.id),
                dict() if poll_question.choices.choices_results is None else json.loads(
                    poll_question.choices.choices_results))
            poll_questions_list.append(single_poll_question_tuple)
            # poll_questions_list.append(
            #     PollForm(poll_question.question_text, question_choices=choices_list, poll_question_id=poll_question.id))
        self.disney_template_render_dict["poll_tuples"] = poll_questions_list
        return self.disney_template_render_dict

    @templated()
    def post(self):
        poll_form = PollForm()
        found_question = PollQuestion.query.get(poll_form.question_id.data)
        if found_question is not None:
            if found_question.choices.choices_results is None:
                found_question.choices.choices_results = json.dumps({f"{poll_form.question.data}": 1})
            else:
                current_results_dict = json.loads(found_question.choices.choices_results)
                if current_results_dict.get(poll_form.question.data) is not None:
                    current_results_dict[poll_form.question.data] += current_results_dict.get(poll_form.question.data)
                else:
                    current_results_dict[poll_form.question.data] = 1
                found_question.choices.choices_results = json.dumps(current_results_dict)
            db.session.commit()
            return redirect(url_for("polls"))
        else:
            Common.create_flash_message("Error occurred recording results")

        return self.disney_template_render_dict
