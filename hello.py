from flask import Flask
from flask import render_template
import berita as br


app = Flask(__name__)


@app.route("/")
@app.route('/detik/')
def detik():
    news = br.indexDetik()
    return render_template('index-detik.html', len=len(news), news=news)


@app.route('/kompas/')
def kompas():
    news = br.indexKompas()
    return render_template('index-kompas.html', len=len(news), news=news)


@app.route('/cnn/')
def cnn():
    news = br.indexCnn()
    return render_template('index-cnn.html', len=len(news), news=news)


@app.route('/sindonews/')
def sindonews():
    news = br.indexSindonews()
    return render_template('index-sindonews.html', len=len(news), news=news)


@app.route('/tribunnews/')
def tribunnews():
    news = br.indexSindonews()
    return render_template('index-tribunnews.html', len=len(news), news=news)
