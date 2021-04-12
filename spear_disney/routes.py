from flask import current_app as spear_disney

from spear_disney.views.home_view import HomeView

home_view = HomeView.as_view(name='home_view')
spear_disney.add_url_rule('/', view_func=home_view, methods=['GET', 'POST'])
