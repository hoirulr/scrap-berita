import urllib
from bs4 import BeautifulSoup

def indexKompas():
    
    tautan = []
    url = "http://indeks.kompas.com/indeks/index/news"
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('h3'):
        
        for l in link.find_all('a'):
            judul = link.get_text()
            isi   = l.get('href')
            berita = {"judul" : judul, "link" : isi}
            tautan.append(berita)
    return tautan


def indexTribunnews():

    tautan = []
    url = "https://www.tribunnews.com/news"
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('h3'):

        for l in link.find_all('a'):
            judul = link.get_text()
            isi = l.get('href')
            berita = {"judul": judul, "link": isi}
            tautan.append(berita)
    return tautan

def indexCnn():
    
    tautan = []
    url = "https://www.cnnindonesia.com/indeks"
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('article'):

        for l in link.find_all('a'):
            judul = link.get_text()
            isi = l.get('href')
            berita = {"judul": judul, "link": isi}
            tautan.append(berita)
    return tautan


def indexDetik():

    tautan = []
    url = "https://news.detik.com/indeks"
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('h3'):

        for l in link.find_all('a'):
            judul = link.get_text()
            isi = l.get('href')
            berita = {"judul": judul, "link": isi}
            tautan.append(berita)
    return tautan

def indexSindonews():
    
    tautan = []
    url = "https://index.sindonews.com/"
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('div', {'class': 'indeks-title'}):

        for l in link.find_all('a'):
            judul = link.get_text()
            isi = l.get('href')
            berita = {"judul": judul, "link": isi}
            tautan.append(berita)
    return tautan

