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


def get_question_number(temp_headers, message, category_id):
    question_number_url = 'https://www.yxgj.net/rest/question/report/' + str(message["id"])

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
    params = {
        "bankid": "31",
        "categoryid": category_id,
        "type": "0"
    }
    # https://www.yxgj.net/rest/question/report/1039652?bankid=31&categoryid=&type=0
    question_number_response = requests.get(question_number_url, params=params, headers=temp_headers, verify=False,
                                            timeout=(10, 30))
    # print('url==', question_number_url)
    # print('参数=', params)
    # print('请求头', temp_headers)
    if (question_number_response.status_code == 200):
        print('获取题目数量成功')
        return question_number_response.text
    else:
        print(question_number_response.status_code)
