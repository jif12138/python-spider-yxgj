import requests
import random
import json
import urllib3
import sys
from bs4 import BeautifulSoup


urllib3.disable_warnings()

def duplicate_detection(one_exam_question_list_new, category_id_1_1):
    one_exam_question_list_new2 = one_exam_question_list_new
    # 获取已经获得的题目ID
    with open("question_result\question_id_" + str(category_id_1_1) + ".json", encoding='utf-8') as fa:
        question_id_list_old = json.load(fa)
        fa.close()
    for question_id_new in one_exam_question_list_new2:
        if question_id_new in question_id_list_old:
            print("题目【", question_id_new, "】已经获得，跳过")
            one_exam_question_list_new.remove(question_id_new)
    if not len(one_exam_question_list_new):
        print("全部以获得，问题列表已清空")
    return one_exam_question_list_new
