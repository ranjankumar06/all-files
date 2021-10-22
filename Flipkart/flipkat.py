# ######################Completed_Flipkat################################

# from bs4 import BeautifulSoup
# import requests
# import json
# from pprint import pprint
# url=("https://www.flipkart.com/search?q=lg+washing+machine&sid=j9e%2Cabm%2C8qx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=lg+washing+machine%7CWashing+Machines+%26+Dryers&requestId=a378c2f9-9a81-418f-8fa4-76115861e7dd&as-searchtext=lg%20washing")
# page= requests.get(url)
# soup= BeautifulSoup(page.text,'html.parser')
# def scrap_flip():
#     main_div=soup.find_all(class_="_4rR01T")
#     a=[]
#     for i in main_div:
#         a.append(i.text)
    
#     price=soup.find_all(class_="_30jeq3 _1_WHN1")
#     c=[]
#     for k in price:
#         c.append(k.text)

#     details=soup.find_all(class_="_1xgFaf")
#     d=[]
#     for b in details:
#         d.append(b.text)

#     dic={}
#     list1=[]
#     for g,m,l in zip(a,c,d):
#         dic["name"]=g
#         # dic["rating"]=h
#         dic["price"]=m
#         dic["details"]=l
#         list1.append(dic.copy())
#     return list1
# x=scrap_flip()
# f=open('flip1.json','w')
# Json_object = json.dump(x,f,indent=4)
# f.close()
