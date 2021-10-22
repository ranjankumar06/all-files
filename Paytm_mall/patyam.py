
# from bs4 import BeautifulSoup
# import requests,json,pprint
# for i in range(1,14):
# url=("https://paytmmall.com/shop/search?q=pickle&from=organic&child_site_id=6&site_id=2&category=101405&page=1&latitude=32.2104220000001&longitude=76.3218640000001")
# page= requests.get(url)
# soup= BeautifulSoup(page.text,'html.parser')

# # def patyam_mall():  

# name=soup.find_all(class_="UGUy")
# a=[]
# for i in name:
#     a.append(i.text)

# price=soup.find_all(class_="_1kMS")
# b=[]
# for j in price:
#     b.append(j.text)


# list2=[]
# for g,m in zip(a,b): 
#     dic={'name':g,'price':m}
#     list2.append(dic)
# pprint.pprint(list2)
# x=patyam_mall()
# pprint.pprint(patyam_mall())

# f=open('paytm.json','w') 
# json_obj=json.dump(x,f,indent=4)
# f.close()






###################################






#####################pataym Mall##############


# from bs4 import BeautifulSoup
# import requests,json,pprint
#  # for i in range(1,14):
# url=("https://paytmmall.com/shop/search?q=pickle&from=organic&child_site_id=6&site_id=2&category=101405")
# page= requests.get(url)
# soup= BeautifulSoup(page.text,'html.parser')

# def patyam_mall():  

#     name=soup.find_all(class_="UGUy")
#     a=[]
#     for i in name:
#         a.append(i.text)

#     price=soup.find_all(class_="_1kMS")
#     b=[]
#     for j in price:
#         b.append(j.text)
#     list2=[]
#     for g,m in zip(a,b): 
#         dic={'name':g,'price':m}
#         list2.append(dic)
#     return list2
# x=patyam_mall()
# # pprint.pprint(patyam_mall())

# f=open('paytm.json','w') 
# json_obj=json.dump(x,f,indent=4)
# f.close()





##########################full_pages########################



#####################pataym Mall##############

from bs4 import BeautifulSoup
import requests,json
from pprint import pprint
list2=[]
for i in range(1,14):
    url=("https://paytmmall.com/shop/search?q=pickle&from=organic&child_site_id=6&site_id=2&category=101405&page="+str(i))
    page= requests.get(url)
    soup= BeautifulSoup(page.text,'html.parser')
    
    name=soup.find_all(class_="UGUy")
    a=[]
    for i in name:
        a.append(i.text)
    price=soup.find_all(class_="_1kMS")
    b=[]
    for j in price:
        b.append(j.text)
    for g,m in zip(a,b): 
        dic={'name':g,'price':m}
        list2.append(dic)
with open('pay.json','w')as f:
    f.write(json.dumps(list2,indent=4))
    f.close()