
# https://www.yxgj.net/rest/exampaperresult/result/2080467


import requests
import random
import json
import urllib3
import sys
from bs4 import BeautifulSoup


urllib3.disable_warnings()

def get_one_exam_question_list(one_exam_id):
    one_exam_id_url = 'https://www.yxgj.net/rest/exampaperresult/question_result/' + str(one_exam_id)
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
    one_exam_question_list = requests.get(one_exam_id_url, headers=temp_headers, verify=False,
                                          timeout=(10, 30))
    # print('url==', question_number_url)
    # print('参数=', params)
    # print('请求头', temp_headers)
    if (one_exam_question_list.status_code == 200):
        print('获取考试试题列表成功')
        question_id_list = []
        for i in json.loads(one_exam_question_list.text)["examQuestionResults"]:
            question_id_list.append(i["questionId"])
        return question_id_list
    else:
        print(one_exam_question_list.status_code)
