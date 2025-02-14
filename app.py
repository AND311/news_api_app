from flask import Flask, request, render_template, jsonify
import requests

# Create a Flask app
app = Flask(__name__)
# url = f"https://newsapi.org/v2/everything?apiKey=8fa5a4dda4cf41549f736ebc451202b6"

@app.route("/")
def index():
    query = request.args.get("query", "latest")
    sources = request.args.get("sources", "")  # Fetch 'sources' from the query parameter

    url = f"https://newsapi.org/v2/everything?apiKey=8fa5a4dda4cf41549f736ebc451202b6&q={query}&language=it&sortBy=publishedAt,popularity"
    if sources != '':
        url += f"&sources={sources}"  

    # Request the news data from NewsAPI
    response = requests.get(url)
    news_data = response.json()

    # Get the list of articles from the response
    articles = news_data.get('articles', [])

    if articles == []:
        url=url.replace('&language=it','')
        response = requests.get(url)
        news_data = response.json()
        articles = news_data.get('articles', [])

    # Render the template and pass the articles to it
    return render_template("index.html", articles=articles)


@app.route("/dropdown")
def dropdown():
    # Fetch sources from NewsAPI
    url = "https://newsapi.org/v2/top-headlines/sources?apiKey=8fa5a4dda4cf41549f736ebc451202b6"
    response = requests.get(url)
    
    if response.status_code == 200:
        sources = response.json().get('sources', [])
        return jsonify(sources)  # Return the sources as a JSON response
    else:
        return jsonify([]), 500  # Return an empty array in case of an error
    
if __name__ == "__main__":
    app.run()
