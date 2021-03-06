# -*- coding: utf-8 -*-
"""WEB SCRAPING PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15epW798u1nKzcOgLW8m32j8Pbe-EFB24
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

url= 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []
time = []
rating = []
metascore =[]
votes = []
gross = []

movie_data = soup.findAll('div', attrs = {'class' :'lister-item mode-advanced'})

for store in Movie_data:
  name = store.h3.a.text
  movie_name.append(name)

  year_of_release = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
  year.append(year_of_release)

  runtime = store.p.find('span', class_ = 'runtime').text.replace(' min','')
  time.append(runtime)

  rate = store.find('div',class_ = 'inline-block ratings-imdb-rating').text.replace('\n','')
  rating.append(rate)

  meta = store.find('span', class_ = 'metascore').text.replace(' ',  '') if store.find('span', class_ = 'metascore') else '^^^^^'
  metascore.append(meta)

  value = store.find_all('span', attrs = {'name': 'nv'})

  vote = value[0].text
  votes.append(vote)

  grosses = value[1].text if len(value) > 1 else '^^^^^^'
  gross.append(grosses)

movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of release': year, 'Watchtime': time, 'Movie Rating': rating, 'Metascore': metascore, 'Votes': votes, 'Gross Collection': gross})

movie_DF.head(70)