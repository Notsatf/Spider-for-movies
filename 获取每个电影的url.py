# -*-codingutf-8-*-
# @Time : 2022/6/22 15:18
# @Author :  TX
# @File : 获取每个电影的url.py
# @Software : PyCharm
import urllib.request
import urllib.parse

#url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=437&page_start=0'

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.119.400 QQBrowser/10.9.4817.400"

}
url_begin = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start="
url_end = "&year_range=2020,2020"
def get_url(url,headers):
    request = urllib.request.Request(url = url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
#保存数据到本地
for i in range(1,40):
    url_final = url_begin + str(i*20) + url_end
    content = get_url(url_final,headers)
    with open('K:\PythonClass\spider_films\json_data\douban2020.json','a+',encoding='utf-8') as fp:
        fp.write(content)
