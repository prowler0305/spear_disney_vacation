from flask.views import MethodView

from spear_disney.decorators import templated
from spear_disney.forms import ChristianSuggestion


class HomeView(MethodView):
    """

    """
    def __init__(self):
        self.christian_suggest_form = ChristianSuggestion()
        self.disney_template_render_dict = dict(christian_suggest_form=self.christian_suggest_form)

    @templated()
    def get(self):
        return self.disney_template_render_dict
