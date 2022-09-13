from operator import imod
import string
from requests import api
from bs4 import BeautifulSoup

page = 0
pagging = 50
animes = []
url = "https://myanimelist.net/topanime.php"


def get_anime_links(res):
    links = []
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.select('tr.ranking-list a'):
        links.append(link.get('href'))
    return links


i = 0


def anime_dataa(list_info):
    for li in list_info:
      print(li.find_one('span.dark_text').string)
    return 0


def get_anime_data(links):
    soup = resp = 0
    # for link in links:
    del resp
    resp = api.get(links[0])
    del soup
    soup = BeautifulSoup(resp.text, 'html.parser')
    lii = soup.select('.spaceit_pad')
    # anime_dataa(lii)
    print(lii)


while i < 5:
    resp = 0
    del resp
    endpoint = url + ('' if not page else '?limit=' + str(page*pagging))
    resp = api.get(endpoint)
    if resp.status_code == 200:
        chunk_anime_links = get_anime_links(resp)
        get_anime_data(chunk_anime_links)
    else:
        break
    i += 1
    pagging += 1
