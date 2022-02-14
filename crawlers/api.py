from urllib.parse import unquote

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from reddit import RedditCrawler

app = Flask(__name__)


@app.route("/redditer", methods=["GET"])
def redditer():
    try:
        categories = unquote(request.args.get("categories"))
        crawler = RedditCrawler(categories.split(";"), 5000)
        content = crawler.content()
        if len(content) == 0:
            return jsonify({}), 404
        return jsonify(content), 200
    except BadRequest:
        app.logger.exception("Bad request")
        return jsonify({}), 400
    except Exception:
        app.logger.exception("Server Error")
        return jsonify({}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
