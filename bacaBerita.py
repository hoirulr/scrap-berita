import urllib
from bs4 import BeautifulSoup


def bacaDetik(url):
    isiBerita = []
    url = urllib.request.urlopen(url)

    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    judul = soup.find('h1', {'class': 'detail__title'}).get_text()
    tanggal = soup.find('div', {'class': 'detail__date'}).get_text()
    for p in soup.find_all('p'):
        isiBerita.append(p.get_text())

    berita = {'judul': judul, 'tanggal' : tanggal, 'isi': isiBerita}
    return berita
