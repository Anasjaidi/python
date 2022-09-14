from requests import api
from bs4 import BeautifulSoup
import time
import json

url = 'https://witanime.com/%d9%82%d8%a7%d8%a6%d9%85%d8%a9-%d8%a7%d9%84%d8%a7%d9%86%d9%85%d9%8a/page/'
resp = soup = 0
page = 1
animeLinks = []
animes = []


def get_anime_links():
    global page, resp, soup
    while page <= 1:
        del resp, soup
        resp = api.get(url+str(page))
        soup = BeautifulSoup(resp.text, 'html.parser')
        animeList = soup.select('.anime-card-container a.overlay')
        for link in animeList:
            animeLinks.append(link['href'])
        page += 1


def get_download(downloads):
  dow = {}
  for ul in downloads:
    quality = str(ul.select_one(':first-child').get_text()).split()[-1]
    dow[quality] = []
    for link in ul.select('li a'):
      dow[quality] = [*dow[quality], {'name':link.get_text(), 'link':link['href']}]
  return(dow)
    

def get_episodes(link):
  next = link
  soup = resp = 0
  episodes = []
  while next:
      obj = {'streams':[]}
      del soup ,resp
      resp = api.get(next).text
      soup = BeautifulSoup(resp, 'html.parser')
      streams = soup.select('#episode-servers li a')
      downloads = soup.select('.episode-download-container .quality-list')
      obj['downloads'] = get_download(downloads)
      for stream in streams:
          obj['streams'] = [*obj['streams'], {'name':stream.get_text(), 'link': stream['data-ep-url']}]
      episodes.append(obj)
      if  soup.select_one('.next-episode a'):
        next = soup.select_one('.next-episode a')['href']
      else:
        next = 0 
  return(episodes)

def get_anime_info():
  global resp, soup
  obj = {'genres':[],}
  for link in animeLinks:
    del resp, soup, obj
    obj = {'genres':[],}
    resp = api.get(link)
    soup = BeautifulSoup(resp.text, 'html.parser')
    obj['img'] = soup.select_one('.anime-thumbnail img')['src']
    obj['title'] = soup.select_one('.anime-details-title').get_text()
    obj['story'] = soup.select_one('.anime-story').get_text()
    obj['episodes'] = get_episodes(soup.select_one('.episodes-card-container a')['href'])
  return obj

# get_anime_links()
animeLinks = ['https://witanime.com/anime/one-piece/']
data = get_anime_info()
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
