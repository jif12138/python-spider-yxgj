# 本项目是为了爬取药学工具王的考试习题
# https://www.yxgj.net/
#

import requests
from bs4 import BeautifulSoup
import os
import json
import random

from PaChong.YaoXueGongJu.main import login

from PaChong.YaoXueGongJu.test import get_question_number
from PaChong.YaoXueGongJu.test import get_one_exam_id
from PaChong.YaoXueGongJu.test import get_one_exam_question_list
from PaChong.YaoXueGongJu.test import get_one_question
from PaChong.YaoXueGongJu.test import cut_one_question
from PaChong.YaoXueGongJu.test import save_questions
from PaChong.YaoXueGongJu.test import save_question_id
from PaChong.YaoXueGongJu.test import duplicate_detection
from PaChong.YaoXueGongJu.test import create_file

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
        'Content - Length': '2',
        'Origin': 'https: // www.yxgj.net ',  #
        'Connection': 'close',  # keep-alive
        'Referer': 'https://www.yxgj.net/index.html',

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
        'Connection': 'close',
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
question_bank = [
    {
        "id": 2,
        "code": "yxtk",
        "name": "药学题库",
        "quantity": 8337,
        "status": 0,
        "memberTypes": "0,1,2,3,4",
        "type": "1,2,3,4,5",
        "createTime": 1537239072000,
        "updateTime": 1555300396000,
        "deleteFlag": 0,
        "createUserid": "",
        "updateUserid": "",
        "memberTypesName": "药师,医生,护士,学生,其他",
        "allMemberTypesNames": "药师,医生,护士,学生,其他",
        "typesName": "单选,多选,处方审核题,用药交代题,用药情景咨询题",
        "allTypes": "单选,多选,填空,实践,处方审核题,用药交代题,用药情景咨询题",
        "doneQuantity": 0,
        "undoneQuantity": 0,
        "isNewestPublish": 0,
        "imageUrl": "/file/201904/ffa428e7-a116-42a2-96c8-88d05317e16b.png"
    },
    {
        "id": 28,
        "code": "111111",
        "name": "省市赛题库（原实践题题库）-第六届中国药师职业技能大赛",
        "quantity": 1205,
        "status": 0,
        "memberTypes": "0",
        "type": "1,2,3,4,5,6",
        "createTime": 1574226183000,
        "updateTime": 1580795728000,
        "deleteFlag": 0,
        "createUserid": "",
        "updateUserid": "",
        "memberTypesName": "药师",
        "allMemberTypesNames": "药师,医生,护士,学生,其他",
        "typesName": "单选,多选,处方审核题,用药交代题,用药情景咨询题,其他题型",
        "allTypes": "单选,多选,填空,实践,处方审核题,用药交代题,用药情景咨询题",
        "doneQuantity": 0,
        "undoneQuantity": 0,
        "isNewestPublish": 1,
        "imageUrl": "/file/201912/fef3b53a-8ee9-4b41-b175-ebaa14210170.png"
    },
    {
        "id": 31,
        "code": "222",
        "name": "第六届药师职业技能大赛—药学知识（下）",
        "quantity": 3931,
        "status": 0,
        "memberTypes": "0",
        "type": "1,2",
        "createTime": 1575366545000,
        "updateTime": 1577958611000,
        "deleteFlag": 0,
        "createUserid": "",
        "updateUserid": "",
        "memberTypesName": "药师",
        "allMemberTypesNames": "药师,医生,护士,学生,其他",
        "typesName": "单选,多选",
        "allTypes": "单选,多选,填空,实践,处方审核题,用药交代题,用药情景咨询题",
        "doneQuantity": 0,
        "undoneQuantity": 0,
        "isNewestPublish": 0,
        "imageUrl": "/file/201912/710afa97-71cc-4905-93bb-91d3afac614d.jpg"
    },
    {
        "id": 39,
        "code": "00000",
        "name": "第六届药师职业技能大赛—药学知识（上）",
        "quantity": 4229,
        "status": 0,
        "memberTypes": "0",
        "type": "1,2",
        "createTime": 1577428460000,
        "updateTime": 1577958602000,
        "deleteFlag": 0,
        "createUserid": "",
        "updateUserid": "",
        "memberTypesName": "药师",
        "allMemberTypesNames": "药师,医生,护士,学生,其他",
        "typesName": "单选,多选",
        "allTypes": "单选,多选,填空,实践,处方审核题,用药交代题,用药情景咨询题",
        "doneQuantity": 0,
        "undoneQuantity": 0,
        "isNewestPublish": 0,
        "imageUrl": "/file/201912/5ef2f429-87ca-49f6-882f-4b707502ea43.png"
    }
]

if __name__ == "__main__":
    ra = random.randint(0, 3)
    temp_headers = headers[ra]
    category_id_1_1 = 452
    # 登录获取session 和 用户id
    message = login.login("https://www.yxgj.net/rest/member/session")
    print("message")
    print(message)
    # 获取对应题目类型的题目数量
    question_number = get_question_number.get_question_number(temp_headers, message, category_id_1_1)
    print(question_number)

    # create_file.createFile(category_id_1_1)
    n = 20
    counter = 1
    while counter <= n:
        counter += 1
        # 获取一场考试的ID
        one_exam_id = get_one_exam_id.get_one_exam_id(temp_headers, message, category_id_1_1)
        print(one_exam_id)
        # 通过考试ID获取该场考试的题目列表
        one_exam_question_list = get_one_exam_question_list.get_one_exam_question_list(temp_headers, message,
                                                                                       one_exam_id)
        print("初步获得的试题编号列表长度=", len(one_exam_question_list))
        print("初步获得的试题编号列表", one_exam_question_list)
        # 去除重复的问题ID
        one_exam_question_list_NO_Repeat = duplicate_detection.duplicate_detection(one_exam_question_list,
                                                                                   category_id_1_1)
        print("去重后获得的试题编号列表长度=", len(one_exam_question_list))
        print("去重后获得的试题编号列表", one_exam_question_list)
        question_list = []
        question_id_list = []
        for one_question_id in one_exam_question_list_NO_Repeat:
            # 通过题目列表中的题目ID逐个获取　题目详细信息
            one_question = get_one_question.get_one_question(temp_headers, message, one_question_id)
            question_cut = cut_one_question.cut_one_question(one_question)
            print(question_cut)
            question_list.append(question_cut)
            question_id_list.append(question_cut["id"])
        save_questions.save_questions(question_list, category_id_1_1)
        save_question_id.save_question_id(question_id_list, category_id_1_1)
        print("添加问题", len(question_list), "个")
        print("添加问题ID", len(question_id_list), "个")
