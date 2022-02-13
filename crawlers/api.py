from quart import Quart, websocket, request

from reddit import RedditCrawler

app = Quart(__name__)


@app.route("/redditer", methods=["GET"])
async def json():
    categories = request.args.get("categories").split()
    crawler = RedditCrawler(categories, 5000)
    return await crawler.content()


@app.websocket("/ws")
async def ws():
    while True:
        await websocket.send("hello")
        await websocket.send_json({"hello": "world"})

if __name__ == "__main__":
    app.run()
