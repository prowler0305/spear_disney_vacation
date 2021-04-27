from flask import current_app as spear_disney

from spear_disney.views.home_view import HomeView
from spear_disney.views.pics_vids import PicsVids
from spear_disney.views.vacation_content import VacationContent

home_view = HomeView.as_view(name="home_view")
content_view = VacationContent.as_view(name="vacation_content")
pics_vids_view = PicsVids.as_view(name="pics_vids")
spear_disney.add_url_rule('/', view_func=home_view)
spear_disney.add_url_rule('/vacation', view_func=content_view, methods=['GET', 'POST'])
spear_disney.add_url_rule('/pics_vids', view_func=pics_vids_view)
