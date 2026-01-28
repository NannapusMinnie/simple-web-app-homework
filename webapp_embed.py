from flask import Flask, render_template, request
import logging

from recommender_embed import find_top_k
from mistral_embed_demo import get_embedding

app = Flask(__name__)

# LOGGING
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# STORAGE
stored_messages = []

# ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []

    if request.method == "POST":
        nickname = request.form["nickname"]
        message = request.form["message"]

        logger.info(
            f"New message added | nickname={nickname} | message={message}"
        )

        # embedding
        embedding = get_embedding(message)

        # similarity ranking
        top3 = find_top_k(embedding, stored_messages, k=3)

        # log similarity
        for item, score in top3:
            logger.info(
                f"Cosine similarity | new_user={nickname} | "
                f"matched_user={item['nickname']} | score={score:.4f}"
            )

        # relevance filter
        for item, score in top3:
            if score > 0.6:
                recommendations.append({
                    "nickname": item["nickname"],
                    "message": item["message"],
                    "score": round(score, 3)
                })

        # store current message
        stored_messages.append({
            "nickname": nickname,
            "message": message,
            "embedding": embedding
        })

    return render_template(
        "embed.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)