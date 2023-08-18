import requests
from bs4 import BeautifulSoup
import csv

# 打开 CSV 文件以进行写入
f = open("游戏版号.csv", mode="w", newline='', encoding='gbk')
csvwriter = csv.writer(f)

url = "https://www.nppa.gov.cn/bsfw/jggs/yxspjg/gcwlyxspxx/202301/t20230118_667079.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"
}

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'

# 创建 BeautifulSoup 对象以解析页面内容
page = BeautifulSoup(response.text, "html.parser")

# 查找所有带有类名 "item" 的 <tr> 元素
trs = page.find_all("tr", class_="item")

# 遍历每个 <tr> 元素
for tr in trs:
    tds = tr.find_all("td")  # 查找当前 <tr> 中的所有 <td> 元素

    # 从 <td> 元素中提取数据
    num = tds[0].text
    name = tds[1].text
    chuban = tds[2].text
    shenbao = tds[3].text
    wenhao = tds[4].text
    wuhao = tds[5].text
    time = tds[6].text

    # 从 <script> 和 <td> 元素中提取值
    script_tag = tr.find("script", language="javascript")
    if script_tag:
        _sblb = script_tag.string
        sblb_start = _sblb.find("var _sblb = '") + len("var _sblb = '")
        sblb_end = _sblb.find("'", sblb_start)
        if sblb_start >= 0 and sblb_end >= 0:
            sblb_value = _sblb[sblb_start:sblb_end]

    csvwriter.writerow([num, name, sblb_value, chuban, shenbao, wenhao, wuhao, time])

# 关闭 CSV 文件
f.close()
