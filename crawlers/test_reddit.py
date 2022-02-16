from unittest import TestCase
from unittest.mock import patch, Mock

from reddit import RedditCrawler


class TestRedditCrawler(TestCase):

    @patch('reddit.webdriver.Firefox')
    @patch('reddit.Service')
    @patch('reddit.Options')
    def test_start_driver(self, options: Mock,
                          service: Mock, web_driver: Mock) -> None:
        RedditCrawler.start_driver()
        options.assert_called_once()
        service.assert_called_once()
        web_driver.assert_called_once()

    @patch('reddit.RedditCrawler.start_driver')
    def test_html_content(self, start_driver: Mock) -> None:
        crawler = RedditCrawler(['cats'], 100)
        content = crawler.html_content()
        start_driver.assert_called_once()
        assert "cats" in content.keys()

    @patch('reddit.RedditCrawler._get_hot_topics')
    @patch('reddit.RedditCrawler.html_content')
    def test_content(self, html_content: Mock, hot_topics: Mock) -> None:
        html_content.return_value = {"cats": "<string>aaa</string>"}
        hot_topics.return_value = [
            {"title": 'lalalala', "score": 5000, "url": "/cats"}
        ]
        crawler = RedditCrawler(['cats'], 100)
        content = crawler.content()
        html_content.assert_called_once()
        hot_topics.assert_called_once()
        assert isinstance(content, dict)
