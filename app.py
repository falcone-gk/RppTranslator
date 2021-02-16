from flask import Flask, render_template, request, redirect
from rpp_scrapper import rpp_news

data = {"title": "",
        "date": "",
        "summary": "",
        "img_url": "",
        "body": ""}

is_scraped = False

app = Flask(__name__)

"""@app.route('/')
def index():
    return render_template('index.html')"""

@app.route('/', methods=['GET', 'POST'])
def scraper():

    global data, is_scraped

    if request.method == 'POST':
        url = request.form['url']
        data = rpp_news(url)
        is_scraped = True
        return redirect("/")

    else:
        return render_template("index.html", data=data, is_scraped=is_scraped)

if __name__ == "__main__":
    app.run(debug=True)