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

# https://www.yxgj.net/rest/question/37286
def get_one_question(temp_headers, message, question_id):
    one_question_url = 'https://www.yxgj.net/rest/question/' + str(question_id)

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
