from urllib.request import urlopen
from multiprocessing import Pool
import os

DDIR = '/home/martin/Downloads/history_of_rome_podcast'

def download_mp3(url):
  fname = os.path.join(DDIR, url.split('/')[-1])
  resp = urlopen(url)
  data = resp.read()
  with open(fname, 'wb') as f:
    f.write(data)


lines = [l.strip() for l in open('mp3links')]

p = Pool(8)
p.map(download_mp3, lines)


