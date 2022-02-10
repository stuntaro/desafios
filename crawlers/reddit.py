from lxml import html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class RedditCrawler:

    def __init__(self, category: str) -> None:
        options = Options()
        options.add_argument("--headless")

        service = Service("/usr/local/bin/geckodriver")

        browser = webdriver.Firefox(service=service, options=options)
        browser.get(f"https://old.reddit.com/r/{category}")

        self._content = html.fromstring(browser.page_source)
        browser.close()

    def get_threads_by_score_limit(self, score: int) -> list[dict]:
        xpath = "//div[@id='siteTable']/"\
                "div[not(contains(@class, 'clearleft'))]"
        self._content.xpath(xpath)
        pass
