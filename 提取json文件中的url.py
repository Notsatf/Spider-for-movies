# -*-codingutf-8-*-
# @Time : 2022/6/22 15:47
# @Author :  TX
# @File : 提取json文件中的url.py
# @Software : PyCharm
import os

from jsonpath import jsonpath
import json

# with open("K:\PythonClass\spider_films\json_data\douban.json", encoding="utf-8") as file:
#     file_json = json.loads(file.readline())
obj = json.load(open('json_data/douban2020.json', 'r', encoding='utf-8'))
urls = jsonpath(obj, "$..url")

# #print(urls)
#print(len(urls))
import requests
from bs4 import BeautifulSoup

#url = "https://movie.douban.com/subject/34839344/"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.119.400 QQBrowser/10.9.4817.400"
}
def get_info(url,headers):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    film_name = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("name")
    director = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("director")
    actors = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("actor")
    film_time = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("datePublished")
    film_gener = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("genre")#电影类型
    film_desc = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("description")
    film_rate = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("aggregateRating")
    image_url = json.loads(soup.find('script', {'type': 'application/ld+json'}).get_text(),strict=False).get("image")
    directors_name = [] #导员
    actors_name = []    #演员
    film_times = [] #上映时间
    film_times.append(film_time)
    film_rates = [film_rate['ratingValue']]
    film_disc = []#电影描述
    film_disc.append(film_desc)
    film_names = []
    film_names.append(film_name)
    for info in range(len(director)):
        directors_name.append(director[info]['name'])
    for info in range(len(actors)):
        actors_name.append(actors[info]['name'])
    film_names = str(film_names)
    directornames = ""
    for i in directors_name:
        directornames += str(i) + " "
    actornames = ""
    for i in actors_name:
        actornames += str(i) + ","
    film_geners = ""
    for i in film_gener:
        film_geners += str(i) + ","
    movietime = ""
    for i in film_times:
        movietime += str(i) + " "
    rate_value = ""
    for i in film_rates:
        rate_value += str(i) + " "
    list2 = [film_name,directornames,actornames,movietime,film_geners,film_desc,rate_value,image_url]
    list1 = ["movie_name","director","actors","movie_time","gener","desc","rate","img_url"]
    dict1 = dict(zip(list1,list2))
    return dict1
for i in urls:
    dict_info = get_info(i,headers=headers)
    with open("json_data/movies_2020.json","a+",encoding='utf-8') as f:
        if  os.path.getsize("json_data/movies2020.json") != 0:
            f.write(",\n")
        json.dump(dict_info,f,skipkeys=False, ensure_ascii=False,indent=2)

