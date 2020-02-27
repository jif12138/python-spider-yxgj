# import requests
#
# r = requests.get('https://www.yxgj.net/')
#
# print(r.status_code)
import requests
import random
import json
import urllib3
import sys
from bs4 import BeautifulSoup

urllib3.disable_warnings()

headers = [
    {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/45.0.2403.155 Safari/537.36',
        'Referer': 'https://www.yxgj.net/index.html'
    },
    {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': 'application/json',
        'Cache- ': 'max-age=0',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Referer': 'https://www.yxgj.net/index.html'
    },
    {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': 'application/json',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.145 Safari/537.36 Vivaldi/2.6.1566.49',
        'Referer': 'https://www.yxgj.net/index.html'
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36 Edg/81.0.410.0',
        'Referer': 'https://www.yxgj.net/index.html'
    },
]

user_pass1 = {"phone": "17152707848", "password": "Jim123456789"}
user_pass2 = {"phone": "17069623004", "password": "Jim123456789"}
user_pass2 = {"phone": "15318838316", "password": "Jim123456789"}


def login(url):
    ra = random.randint(0, 3)
    temp_headers = headers[ra]
    content = temp_headers["User-Agent"]
    version = content.split(' ')[-1].split('/')[-1]
    manufacturer = content.split(' ')[-1].split('/')[0]
    data = {"content": content, "mobileOS": "web",
            "version": version, "manufacturer": manufacturer}
    data.update(user_pass1)
    # print(type(data))
    # print(data)
    # print(type(json.dumps(data)))
    # print(data)
    r = requests.post(url, data=json.dumps(data), headers=temp_headers, verify=False, timeout=(10, 30))

    print("获取session",r.status_code)
    if r.status_code == 200:
        print(r.json())
        message = r.json()
        temp_headers["Cookie"] = \
            "id=" + str(message["id"]) + \
            "; session_id=" + message["session_id"] + \
            "; username=" + str(message["username"]) + \
            "; phone_number=" + str(message["phone_number"]) + \
            "; type=" + message["type"] + \
            "; assessment=" + str(message["roleList"]["assessment"]) + \
            "; competition_audit=" + str(message["roleList"]["competition_audit"]) + \
            "; course=" + str(message["roleList"]["course"]) + \
            "; learning=" + str(message["roleList"]["learning"]) + \
            "; mark=" + str(message["roleList"]["mark"]) + \
            "; student=" + str(message["roleList"]["student"]) + \
            "; subject=" + str(message["roleList"]["subject"])

        print(["Cookie"])
        print(temp_headers["Cookie"])
        index_url = "https://www.yxgj.net/index.html#questions_bank"
        index_r = requests.post(index_url, headers=temp_headers, verify=False, timeout=(10, 30))
        print(index_r.status_code)
        if index_r.status_code == 200:
            index_soup = BeautifulSoup(index_r.content, 'html.parser')
            # print(index_soup.prettify().encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
        return message


# 获取题库题目类别
# https://www.yxgj.net/rest/category/get-list?type=2&key=&offset=0&rows=50000&questionBankId=31&questionType=0


# 获取题目列表
# https://www.yxgj.net/rest/exampaperresult/result/2079184

if __name__ == "__main__":
    login("https://www.yxgj.net/rest/member/session")

# {"JSON":{"member_type":0,"vip_end_time":null,"avatar_url":null,"vip_grade":0,"vip_name":"","session_id":"M-d27278da298b428c81c36cd3","phone_number":"15318838316","id":1039652,"type":"member","roleList":{"assessment":"0","student":"1","subject":"0","course":"0","learning":"0","mark":"0","competition_audit":"0"},"username":"15318838316"}}
# Cookie: id=1039652; session_id=M-758bbaafa57c4f4688b1bc97; username=15318838316; phone_number=15318838316; type=member; assessment=0; competition_audit=0; course=0; learning=0; mark=0; student=1; subject=0
