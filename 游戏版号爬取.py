import requests
from bs4 import BeautifulSoup
import csv

#拿到页面源代码
f = open("游戏版号.csv",mode="w")
csvwriter = csv.writer(f)
url = "https://www.nppa.gov.cn/bsfw/jggs/yxspjg/gcwlyxspxx/202306/t20230621_718323.html"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"
}

response = requests.get(url = url,headers = headers)
response.encoding = 'utf-8'
# print(response.text)

#解析数据
#1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(response.text,"html.parser") #指定html解析器
#2.从bs对象中查找数据
#find(标签， 属性=值)：第一个 find_all(标签， 属性=值)：全部
# table = page.find("table",width='100%') #class是python关键字,若为class改为class_
table = page.find("table",attrs={"width":"100%"}) #和上一行同一个意思，可以避免class
# print(table)
#拿到所有数据
trs = table.find_all("tr")[1:] #tr是行，td是列
for tr in trs: #每一行
    tds = tr.find_all("td") #拿到每行中的所有td
    num = tds[0].text #.text表示拿到被标签标记的内容
    name = tds[1].text
    chuban = tds[2].text
    shenbao = tds[3].text
    wenhao = tds[4].text
    wuhao = tds[5].text
    time = tds[6].text
    csvwriter.writerow([num,name,chuban,shenbao,wenhao,wuhao,time])
f.close()