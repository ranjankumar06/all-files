import json,os
from task1 import scrap_top_list
def scrape_movie_details(pr):
    for i in pr:
        lis=i["url"]
        listid=str(lis[27:-1])+".json"
        if not(os.path.exists(listid)):
            f=open(f"{listid}.json",'w+')
            json.dump(i,f,indent=4)
            f.close()
            print("not exists")
        else:
            print("alrady exists")
task8 = scrap_top_list()
scrape_movie_details(task8)
