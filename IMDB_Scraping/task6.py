# from bs4 import BeautifulSoup
# from task5 import*
import json
from pprint import pprint
a=open("scraping5.json","r")
b=json.load(a)
a.close()
def analyse_movies_language(movie):
    c={}
    for i in b:
        for j in i["language"]:
            if (j not in c):
                c[j]=0
    for j in c:
        for k in movie:
            for m in k["language"]:
                if (m==j):
                    c[j]+=1
    file=open('scraping_6.json','w')
    json.dump(c,file,indent=4)
    file.close()
    return c
task6=analyse_movies_language(b)
pprint(task6)