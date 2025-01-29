from flask import Flask, request, render_template
import requests
# from config import NEWS_API_KEY



#Create a flask app
app = Flask(__name__)


# Homepage - Route 8fa5a4dda4cf41549f736ebc451202b6
# Home / About / Contact / Pricing


@app.route("/")
def index():
    query = request.args.get("query","latest")
    url = f"https://newsapi.org/v2/everything?q={query}&language=it&apiKey=8fa5a4dda4cf41549f736ebc451202b6"
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get('articles', [])
        
    return render_template("index.html", articles=articles)


if __name__ == "__main__":
    app.run()