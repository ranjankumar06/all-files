from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
url=("https://www.imdb.com/india/top-rated-indian-movies/")
page= requests.get(url)
soup= BeautifulSoup(page.text,'html.parser')

def scrap_top_list():
    main_div = soup.find ('div' , class_='lister')
    tbody= main_div.find('tbody',class_='lister-list')
    trs = tbody.find_all ('tr')

    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]
    for tr in trs:
        position = tr.find('td',class_="titleColumn").get_text().strip()
        rank=''
        for  i in position:
            if '.' not in i:
                rank = rank + i  
            else:
                break
        movie_ranks.append(rank)

        titel=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(titel)

        year= tr.find('td',class_="titleColumn").span.get_text()
        year_of_realease.append(year)

        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)

        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="http://www.imdb.com%26quot%3B/ + link"
        movie_urls.append(movie_link)
    Top_Movies=[]
    details={'position':'','name':'','year':'','rating':'','url':''}
    for i in range(0,len(movie_ranks)):
        details['position']=int(movie_ranks[i])
        details['name'] = str (movie_name[i])
        year_of_realease[i] = year_of_realease[i][1:5]
        details['year']= int(year_of_realease[i])
        details['rating'] = float (movie_ratings[i])
        details['url']= movie_urls[i]
        Top_Movies.append(details.copy())
    return (Top_Movies)
scrapped=scrap_top_list()
x=scrap_top_list()
f=open('task.json','w')
Json_object = json.dump(x,f,indent=4)
f.close()

