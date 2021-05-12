import json
from collections import namedtuple
from datetime import datetime
from typing import Union


from flask import flash, current_app as eoc_app
from requests import Response
from sqlalchemy.orm import Query


class Common(object):
    """
    Common class that encapsulates generic static methods that can provide common functionality.
    """

    @staticmethod
    def create_flash_message(message: Union[Response, str] = None, category_request: tuple = ('base', 'info'),
                             add_issue_request_message=False) -> flash:
        """
        Creates a flask flash message object that can be used on the next HTTP request.

        'category_request' parameter is used by the UI HTML template code. A tuple that consists of a string identifier
        that can be as a unique way of retrieve flash messages via get_flashed_messages() so that they are only
        displayed in that display block.

        The second value of the tuple can be set to any value but when set to one of the possible Bootstrap coloring
        keywords it can be used to dynamically set the color of the Bootstrap component being used to display the
        retrieved message. (e.g. an alert-dialog component)

        For example: these keywords could be used to indicate the severity of a message.
              'success'(green) - A action completed successfully without issues
              'info'(blue) - For general information
              'warning'(yellow) - For warnings
              'danger'(red) - For errors
              'dark'(black) - For severe/critical internal errors

        HTML Template Example:

            {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                    {% for category, message in messages %}
                        {% if category[0] == 'some_unique_string_identifier' %}
                            <div class="row mt-1">
                                <div class="alert alert-{{ category[1] }} alert-dismissible fade show" role="alert">
                                    {{ message }}
                                    <button type="button" class="close" data-dismiss="alert" aria-label="close">
                                        <span aria-hidden="true">&times</span>
                                    </button>
                                </div>
                            </div>
                        {% endif %}
                    {% endfor %}
                {% endif %}
            {% endwith %}

        :param message: Can be a string or an HTTP response object in which the response text which should contain the
        standard HTTP error text will be extracted as the message
        :param category_request :type Tuple:  (unique string identifier, bootstrap color keyword)
        :param add_issue_request_message: Adds the request fo an issue ticket to be submitted to the message. (Default: False)
        :return: Flash object that was created.
        """

        CategoryRequest = namedtuple("CategoryInfoTuple", ['identifier', 'color'])
        category_info = CategoryRequest._make(category_request)
        request_issue_message = ""
        if add_issue_request_message:
            request_issue_message = "Please submit an issue ticket to the SA3 Core Automation Team."
        if isinstance(message, Response):
            if 'message' in message:
                message_dict = json.loads(message)
            else:
                message_dict = dict(message=None)
                message_dict['message'] = str("{}:{} {}".format(message.status_code, message.reason,
                                                                request_issue_message))
            return flash(message_dict['message'], category=category_info._asdict())
        else:
            if message is None:
                message = 'Unknown internal error has occurred.'
            return flash("{} {}".format(message, request_issue_message), category=category_info._asdict())
