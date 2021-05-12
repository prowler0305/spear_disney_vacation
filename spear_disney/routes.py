from flask import current_app as spear_disney

from spear_disney.views.home_view import HomeView
from spear_disney.views.pics_vids import PicsVids
from spear_disney.views.polling.add_polls import AddPoll
from spear_disney.views.polling.polls import Polls
from spear_disney.views.vacation_requests import VacationRequests

home_view = HomeView.as_view(name="home_view")
requests_view = VacationRequests.as_view(name="vacation_requests")
poll_view = Polls.as_view(name="polls")
pics_vids_view = PicsVids.as_view(name="pics_vids")
add_polls_view = AddPoll.as_view(name="add_poll")
spear_disney.add_url_rule('/', view_func=home_view)
spear_disney.add_url_rule('/vacation_requests', view_func=requests_view, methods=['GET', 'POST'])
spear_disney.add_url_rule('/polls', view_func=poll_view, methods=['GET', 'POST'])
spear_disney.add_url_rule('/pics_vids', view_func=pics_vids_view)
spear_disney.add_url_rule('/add_poll', view_func=add_polls_view)
