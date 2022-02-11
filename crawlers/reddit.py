import json
import logging
from time import time

from lxml import html
from collections import defaultdict
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)

log = logging.getLogger(__name__)


def write_json(content: dict) -> None:
    file_name = f"/var/tmp/{time()}.json"
    with open(file_name, "w") as f:
        f.write(json.dumps(content, indent=4, sort_keys=True))


class RedditCrawler:

    def __init__(self, categories: list, score: int) -> None:
        self._categories = categories
        self._score = score
        options = Options()
        options.add_argument("--headless")
        service = Service("/usr/local/bin/geckodriver")

        self.browser = webdriver.Firefox(service=service, options=options)

    def content(self) -> dict:
        data = defaultdict(list)
        for category in self._categories:
            self.browser.get(f"https://old.reddit.com/r/{category}")
            content = html.fromstring(self.browser.page_source)
            for thread in self._get_threads_by_score_limit(content):
                thread["url"] = urljoin("https://reddit.com", thread["url"])
                data[category].append(thread)
        self.browser.close()
        return data

    def _get_threads_by_score_limit(self, content) -> iter:
        xpath = "//div[@id='siteTable']/"\
                "div[not(contains(@class, 'clearleft'))]"
        for thread in content.xpath(xpath)[:-1]:
            try:
                score = int(thread.xpath("@data-score")[0])
                if score < self._score:
                    continue
                link = thread.xpath("@data-permalink")[0]
                title_xpath = "div/div/p[@class='title']/a"\
                              "[@data-event-action='title']/text()"
                title = thread.xpath(title_xpath)[0]
                yield {"title": title, "score": score, "url": link}
            except IndexError:
                log.exception(html.tostring(thread))


if __name__ == "__main__":
    crawler = RedditCrawler(["askreddit", "worldnews", "cats"], 5000)
    write_json(crawler.content())
