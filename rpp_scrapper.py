import requests
from bs4 import BeautifulSoup

def rpp_news(url):
    """
    Scrap the content news and image from the url which must be from Rpp webpage.

    Parameters
    ----------

    url: string
        It is the news url from Rpp webpage.
    """

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Getting headers elements.
    header = soup.find('header', class_='story-header')
    title = header.find('h1').text
    date = header.find('time')['datetime']
    summary = header.find('div', class_='sumary').find('p').text

    # Getting image cover.
    img_url = soup.find('div', class_='cover').find('img')['src']

    # Getting news body.
    body = [p.text for p in soup.find(id='article-body').find_all('p')]

    return {
        "title": title,
        "date": date,
        "summary": summary,
        "img_url": img_url,
        "body": body
    }

def main():
    val = rpp_news('https://rpp.pe/politica/gobierno/francisco-sagasti-martin-vizcarra-cambia-de-version-y-pone-en-tela-de-juicio-todo-el-proceso-de-prueba-de-las-vacunas-noticia-1320932')

if __name__ == '__main__':
    main()