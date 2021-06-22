from flask import Flask
from flask import render_template
import berita as br


app = Flask(__name__)


@app.route("/")
@app.route('/hello/')
@app.route('/hello/<name>')
def hello():
    news = br.indexSindonews()
    
    return render_template('test.html', len=len(news), news=news)
