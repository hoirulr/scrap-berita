import urllib
from bs4 import BeautifulSoup
import datetime
from datetime import date

url = "http://indeks.kompas.com/indeks/index/news"

#ambil hari ini
today = date.today().strftime("%d%m%Y")
filename = "brt-%s.txt" % today
filelink = "link-%s.txt" % today

def getUrl(url):
    '''ambil url tiap berita di indeks'''
    tautan = []
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('h3'):
        for l in link.find_all('a'):
            isi = l.get('href')
            tautan.append(isi)
    return tautan


def getIndeks(url):
    i = 1
    tautans = []
    tautan = getUrl(url)
    while (len(tautan) != 0 and i < 2):
        url = "http://indeks.kompas.com/indeks/index/news?p=%d" % i
        print (url)
        i += 1
        tautan = getUrl(url)
        tautans += tautan

    print (len(tautans))
    bf = open(filelink, "w")
    for t in tautans:
        bf.write(t)
        bf.write("\n")
    bf.close()


def getBerita(url):
    url = urllib.request.urlopen(url)
    result = url.read()
    url.close()
    isiberita = ""

    soup = BeautifulSoup(result, "html.parser")
    for berita in soup.find_all('div', {'class': 'read__content'}):
        # isiberita += berita.get_text().encode("utf-8")
        isiberita += berita.get_text()
    bf = open(filename, 'a')
    bf.write(isiberita)
    bf.write("\n")
    bf.close()


def getLinkFromFile():
    '''Ambil berita dari link yang sudah disimpan di link-tgl.txt'''
    print ("Ambil berita dari link tanggal %s. " % today)
    bf = open(filelink, 'r')
    i = 0
    for l in bf:
        print (l)
        getBerita(l)
    bf.close()


#mainkan
getIndeks(url)
getLinkFromFile()
