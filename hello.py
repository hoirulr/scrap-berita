from flask import Flask, redirect
from flask import render_template
from flask import request
import berita as br
import bacaBerita as bb


app = Flask(__name__)


@app.route("/")
@app.route('/detik/')
def detik():
    news = br.indexDetik()
    return render_template('index-detik.html', len=len(news), news=news)


@app.route('/baca-detik', methods=['GET', 'POST'])
def baca_detik():
    if request.method == 'POST':
        url = request.form['url']
        news = bb.bacaDetik(url)
        return render_template('baca-detik.html', news=news, len = len(news['isi']))
    else:
        return redirect("http://localhost:5000")

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
