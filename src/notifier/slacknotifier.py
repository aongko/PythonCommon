import json
import logging
import re
import requests


class SlackNotifier(object):
    """For notify something to Slack"""
    def __init__(self, url, channel, username, debug=False):
        super(SlackNotifier, self).__init__()
        self.LOG = logging.getLogger(__name__)
        self.url_regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if self.check_url(url) is False:
            raise ValueError("not a valid URL")

        self.url = url
        self.channel = channel
        self.username = username
        self.debug = debug

    def notify(self, text, username=None, channel=None, url=None):
        if username is None:
            username = self.username
        if channel is None:
            channel = self.channel
        if url is None:
            url = self.url
        if text is None:
            raise ValueError("text cannot be None")
        if self.check_url(url) is False:
            raise ValueError("not a valid URL")

        payload = {
            "text": text,
            "username": re.sub('[^0-9a-zA-Z]+', '-', username),
            "channel": channel
        }

        if self.debug:
            self.LOG.debug("Payload: %s", str(payload))
            return

        try:
            response = requests.post(url, data=json.dumps(payload))
            self.LOG.debug("Slack response: %s", str(response))
        except Exception as e:
            self.LOG.exception("Unexpected error while sending data to Slack")
            raise e

    def check_url(self, url):
        return False if self.url_regex.match(url) is None else True
