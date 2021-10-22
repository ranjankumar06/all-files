from bs4 import BeautifulSoup
import requests
from task1 import*
from task4 import*
import json,requests
from pprint import pprint
def get_movie_list_details(top_movie):
    movie_details_list=[]
    for i in range(len(top_movie)):
        url=task1[i]["url"]
        a=movie_details(url)
        movie_details_list.append(a.copy())
    f=open("scraping5.json",'w')
    json.dump(movie_details_list,f,indent=4)
    return movie_details_list
task5=get_movie_list_details(url[0:10])
# pprint(task5)



####################################################################################################


