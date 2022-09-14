from operator import imod
import json
import re
from translate import Translator
import translators as ts
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


def anime_dataa(list_info, link):
    obj = {'link': link, 'genres': [], 'titles':{}}
    for li in list_info:
        if li.string in ['Synonyms:', 'Episodes:', 'Status:', 'Rating:', 'Duration:', 'Source:']:
            obj.update({str(li.string).lower()[:-1]: str(li.next_sibling).strip(' \n')})
        elif li.string in ['Type:', 'Premiered:', 'Studios:']:
            obj.update({str(li.string).lower()[:-1]: str(li.next_sibling.next_sibling.string)})
        elif li.string in ['Japanese:', 'English:', 'French:']:
            obj['titles'] = ({**obj['titles'], str(li.string).lower()[:-1]: str(li.next_sibling).strip(' \n')})
        elif li.string == 'Broadcast:':
            obj.update({'broadcast': str(' '.join(li.next_sibling.strip(' \n').split()[0:3]))})
        elif li.string == 'Score:':
            obj.update({'score': float(li.next_sibling.next_sibling.string)})
        elif li.string == 'Genres:':
            for l in li.find_next_siblings("a"):
                obj['genres'] = [x for x in obj['genres']] + [str(ts.bing(str(l.string), to_language='ar'))]
    return(obj)


def get_anime_data(links):
    soup = resp = 0
    # for link in links:
    del resp
    resp = api.get(links[0])
    del soup
    soup = BeautifulSoup(resp.text, 'html.parser')
    li = soup.select('.spaceit_pad span')
    obj = anime_dataa(li, links[0])
    obj = {**anime_dataa(li, links[0]), **{'descrption': soup.find('p', {})}}
    # print(json.dumps(obj))
    print(obj)


resp = endpoint = chunk_anime_links = 0
def get_anime_links():
    while i < 2:
        del resp, endpoint, chunk_anime_links
        endpoint = url + ('' if not page else '?limit=' + str(page*pagging))
        resp = api.get(endpoint)
        if resp.status_code == 200:
            chunk_anime_links = get_anime_links(resp)
            get_anime_data(chunk_anime_links)
        else:
            break
        i += 1
        pagging += 1

print(get_anime_links())