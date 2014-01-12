""" 
Program to scrape the mp3 links to the history of rome podcast from
the archive page. It only scrapes the links to the mp3 files, which 
can be output into a file and downloaded with another script. Note 
that some (about 3) of the links are to a different domain and the 
list may need to be manually cleaned to remove these anomalies.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool
import re

def flatten(list_of_lists):
  return [item for subl in list_of_lists for item in subl]

def scrape_page(link):
  soup = BeautifulSoup(urlopen(link))
  links = soup.find_all('a', href=re.compile("^.*\.mp3"))
  return list(map(lambda l: l['href'], links))

soup = BeautifulSoup(urlopen('http://thehistoryofrome.typepad.com/the_history_of_rome/archives.html'))

al = soup.find('ul', 'archive-list')
pages = list(map(lambda x: x['href'], al.find_all('a')))


p = Pool(6)
r = p.map(scrape_page, pages)
print("\n".join(flatten(r)))

