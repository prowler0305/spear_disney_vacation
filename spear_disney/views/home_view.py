from flask.views import MethodView
from flask import current_app as spear_app, redirect, url_for
from spear_disney.decorators import templated


class HomeView(MethodView):
    """

    """
    def __init__(self):
        pass

    @templated()
    def get(self):
        return
