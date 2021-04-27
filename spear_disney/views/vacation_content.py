from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for
from spear_disney.decorators import templated
from spear_disney.forms import Suggestion
from spear_disney.models import Suggestions, db


class VacationContent(MethodView):
    """

    """
    def __init__(self):
        self.suggest_form = Suggestion()
        self.disney_template_render_dict = dict(suggest_form=self.suggest_form)
        self.disney_template_render_dict["christian_suggestions"] = Suggestions.query.filter_by(by_who="christian").all()
        self.disney_template_render_dict["sarah_suggestions"] = Suggestions.query.filter_by(by_who="sarah").all()
        self.disney_template_render_dict["mom_suggestions"] = Suggestions.query.filter_by(by_who="mom").all()
        self.disney_template_render_dict["dad_suggestions"] = Suggestions.query.filter_by(by_who="dad").all()

    @templated()
    def get(self):
        return self.disney_template_render_dict

    @templated()
    def post(self):
        if self.suggest_form.submit.data:
            new_suggestion = Suggestions(self.suggest_form.by_who.data, self.suggest_form.suggestion.data,
                                         self.suggest_form.suggestion_category.data)
            db.session.add(new_suggestion)
        elif self.suggest_form.delete_entry.data:
            entry_to_delete = Suggestions.query.get(self.suggest_form.delete_id.data)
            db.session.delete(entry_to_delete)

        db.session.commit()

        return redirect(url_for("vacation_content"))
