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
        'Host': 'www.yxgj.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/45.0.2403.155 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',

        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'role': 'undefined',
        'type': 'member',
        'If-Modified-Since': '0',
        'Cache-Control': 'max-age=0',
        'X-Requested-With': 'XMLHttpRequest',
        'Content - Length': '2',  # get_one_exam_id
        'Origin': 'https: // www.yxgj.net ',  #
        'Connection': 'close',  # keep-alive
        'Referer': 'https://www.yxgj.net/index.html',

        'type': 'member',
        'TE': 'Trailers'

    },
    {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': 'application/json',
        'Cache-Control ': 'max-age=0',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Referer': 'https://www.yxgj.net/index.html',
        'Host': 'www.yxgj.net',
        'Accept-Encoding': 'gzip, deflate, br',
        'role': 'undefined',
        'type': 'member',
        'If-Modified-Since': '0',
        'X-Requested-With': 'XMLHttpRequest',

        'Content - Length': '2',  #
        'Origin': 'https: // www.yxgj.net ',  #
    },
    {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': 'application/json',
        'Cache-Control': 'max-age=0',
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.145 Safari/537.36 Vivaldi/2.6.1566.49',
        'Referer': 'https://www.yxgj.net/index.html',
        'Host': 'www.yxgj.net',
        'Accept-Encoding': 'gzip, deflate, br',
        'role': 'undefined',
        'type': 'member',
        'If-Modified-Since': '0',
        'X-Requested-With': 'XMLHttpRequest',
        'Content - Length': '2',  #
        'Origin': 'https: // www.yxgj.net ',  #
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4041.0 Safari/537.36 Edg/81.0.410.0',
        'Referer': 'https://www.yxgj.net/index.html',
        'Host': 'www.yxgj.net',
        'Accept-Encoding': 'gzip, deflate, br',
        'role': 'undefined',
        'type': 'member',
        'If-Modified-Since': '0',
        'X-Requested-With': 'XMLHttpRequest',
        'Content - Length': '2',  #
        'Origin': 'https: // www.yxgj.net ',  #
    },
]


# https://www.yxgj.net/rest/question/37286
def get_one_question(message, question_id):
    one_question_url = 'https://www.yxgj.net/rest/question/' + str(question_id)
    ra = random.randint(0, 3)
    temp_headers = headers[ra]
    temp_headers["id"] = str(message["id"])
    temp_headers["session_id"] = str(message["session_id"])
    temp_headers["Cookie"] = \
        "Hm_lvt_86a0f368ae62844f36dc0cce47c3d644=1582434157,1582437881,1582447078,1582472646;" + \
        "Hm_lpvt_86a0f368ae62844f36dc0cce47c3d644=1582475602;" + \
        "id=" + str(message["id"]) + \
        "; session_id=" + message["session_id"] + \
        "; username=" + (message["username"]) + \
        "; phone_number=" + str(message["phone_number"]) + \
        "; type=" + message["type"] + \
        "; assessment=" + str(message["roleList"]["assessment"]) + \
        "; competition_audit=" + str(message["roleList"]["competition_audit"]) + \
        "; course=" + str(message["roleList"]["course"]) + \
        "; learning=" + str(message["roleList"]["learning"]) + \
        "; mark=" + str(message["roleList"]["mark"]) + \
        "; student=" + str(message["roleList"]["student"]) + \
        "; subject=" + str(message["roleList"]["subject"])

    # https://www.yxgj.net/rest/question/report/1039652?bankid=31&categoryid=&type=0
    one_question_response = requests.get(one_question_url, headers=temp_headers, verify=False,
                                         timeout=(10, 30))
    if (one_question_response.status_code == 200):
        print('获取试题成功')

        return one_question_response.text
    else:
        print(one_question_response.status_code)
