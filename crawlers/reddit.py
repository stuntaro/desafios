import argparse
import json
import logging

from time import time

from lxml import html
from collections import defaultdict
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format, level=logging.DEBUG)

log = logging.getLogger(__name__)


def write_json(content: dict) -> None:
    file_name = f"{time()}.json"
    with open(file_name, "w") as f:
        f.write(json.dumps(content, indent=4, sort_keys=True))


class RedditCrawler:

    def __init__(self, categories: list, score: int) -> None:
        self._categories = categories
        self._score = score

    @staticmethod
    def start_driver() -> WebDriver:
        options = Options()
        options.add_argument("--headless")
        service = Service("/usr/bin/geckodriver")
        return webdriver.Firefox(service=service, options=options)

    def html_content(self) -> dict:
        browser = self.start_driver()
        contents = defaultdict(str)
        for category in self._categories:
            browser.get(f"https://old.reddit.com/r/{category}")
            contents[category] = self.browser.page_source
        browser.quit()
        return contents

    def content(self) -> dict:
        data = defaultdict(list)
        html_content = self.html_content()
        for category in html_content:
            lxml = html.fromstring(html_content[category])
            for thread in self._get_hot_topics(lxml):
                thread["url"] = urljoin("https://reddit.com", thread["url"])
                data[category].append(thread)
        return data

    def _get_hot_topics(self, content) -> iter:
        xpath = "//div[@id='siteTable']/"\
                "div[not(contains(@class, 'clearleft'))]"
        for thread in content.xpath(xpath)[:-1]:
            try:
                score = thread.xpath("@data-score")
                if len(score) == 0 or int(score[0]) < self._score:
                    continue
                score = int(score[0])
                link = thread.xpath("@data-permalink")[0]
                title_xpath = "div/div/p[@class='title']/a"\
                              "[@data-event-action='title']/text()"
                title = thread.xpath(title_xpath)[0]
                yield {"title": str(title), "score": score, "url": link}
            except IndexError:
                log.exception(html.tostring(thread))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("categories")
    args = parser.parse_args()
    crawler = RedditCrawler(args.categories.split(";"), 5000)
    write_json(crawler.content())
