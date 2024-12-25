from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_text = request.form.get("user_text")
        if user_text.strip():
            blob = TextBlob(user_text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            return render_template(
                "index.html",
                sentiment=sentiment,
                polarity=polarity,
                subjectivity=subjectivity,
                user_text=user_text,
            )
        else:
            return render_template(
                "index.html",
                error="Please enter valid text for analysis.",
                user_text="",
            )
    return render_template("index.html", user_text="")

if __name__ == "__main__":
    app.run(debug=True)
