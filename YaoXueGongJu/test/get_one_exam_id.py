# https://www.yxgj.net/rest/exampaperresult/practice/0?type=2&count=20&bankId=31&categoryId=452#
import requests
import random
import json
import urllib3
import sys
from bs4 import BeautifulSoup


urllib3.disable_warnings()

def get_one_exam_id(temp_headers, message, category):
    params = {
        "type": "0",
        "count": "50",
        "bankId": "31",
        "categoryId": category,  # 452 慢病 459 抗肿瘤
    }
    one_exam_id_url = 'https://www.yxgj.net/rest/exampaperresult/practice/0'

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
    one_exam_id_response = requests.post(one_exam_id_url, params=params, headers=temp_headers, verify=False,
                                         timeout=(10, 30))
    # print('url==', question_number_url)
    # print('参数=', params)
    # print('请求头', temp_headers)
    if (one_exam_id_response.status_code == 200):
        print('获取考试ID成功')
        return json.loads(one_exam_id_response.text)["id"]
    else:
        print(one_exam_id_response.status_code)


