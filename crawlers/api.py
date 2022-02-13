import json

from urllib.parse import unquote

from flask import Flask, request

from reddit import RedditCrawler

app = Flask(__name__)


@app.route("/redditer", methods=["GET"])
def redditer():
    categories = unquote(request.args.get("categories"))
    crawler = RedditCrawler(categories.split(";"), 5000)
    return json.dumps(crawler.content(), indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
