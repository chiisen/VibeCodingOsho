import json
import os
import random
from datetime import datetime
from functools import lru_cache

from flask import Flask, render_template, session, redirect, url_for, request


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    # 開發用預設金鑰，正式環境請用環境變數覆蓋
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

    @lru_cache(maxsize=1)
    def get_cards() -> list[dict]:
        """載入並快取卡牌資料。"""
        data_path = os.path.join(os.path.dirname(__file__), "data", "cards.json")
        with open(data_path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        return payload.get("cards", [])

    def add_history(entry: dict) -> None:
        history = session.get("history", [])
        # 最新在前，最多保存 50 筆
        history.insert(0, entry)
        session["history"] = history[:50]

    @app.after_request
    def add_cache_headers(resp):  # type: ignore[override]
        # 靜態資源長快取
        if request.path.startswith("/static/"):
            resp.headers["Cache-Control"] = "public, max-age=604800, immutable"
        return resp

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/draw", methods=["POST", "GET"])
    def draw():
        cards = get_cards()
        if not cards:
            # 沒有卡牌資料時回首頁並提示（簡化處理，可擴充為閃訊息）
            return redirect(url_for("index"))

        card = random.choice(cards)
        entry = {
            "name": card.get("name"),
            "suit": card.get("suit"),
            "key": card.get("key"),
            "meaning": card.get("meaning"),
            "time": datetime.utcnow().isoformat() + "Z",
        }

        session["last_result"] = entry
        add_history(entry)
        return redirect(url_for("result"))

    @app.route("/result")
    def result():
        result_entry = session.get("last_result")
        if not result_entry:
            return redirect(url_for("index"))
        return render_template("result.html", result=result_entry)

    @app.route("/history")
    def history():
        history_entries = session.get("history", [])
        return render_template("history.html", history=history_entries)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", 5000)),
        debug=True,
    )


