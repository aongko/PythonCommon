import unittest
from notifier.slacknotifier import SlackNotifier

class TestSlackNotifier(unittest.TestCase):

    def test_check_url(self):
        url = "some url"
        channel = "channel_name"
        username = "username"
        with self.assertRaises(ValueError):
            SlackNotifier(url, channel, username)

    def test_no_text(self):
        url = "https://hooks.slack.com/services/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"
        channel = "#data_bot"
        username = "data_bot"
        notifier = SlackNotifier(url, channel, username)
        with self.assertRaises(ValueError):
            notifier.notify(text=None)

if __name__ == '__main__':
    unittest.main()
