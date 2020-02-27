# 本项目是为了爬取药学工具王的考试习题
# https://www.yxgj.net/
#

import requests
from bs4 import BeautifulSoup
import os
import json
import random

from PaChong.YaoXueGongJu.main import login

# from PaChong.YaoXueGongJu import get_question_number
# from PaChong.YaoXueGongJu import get_one_exam_id
# from PaChong.YaoXueGongJu import get_one_exam_question_list
# from PaChong.YaoXueGongJu import get_one_question

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
question_category = [
    {
        "id": 447,
        "code": "ekyy",
        "name": "儿科用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367024000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 26,
        "childs": "",
        "questionNumber": 200
    }, {
        "id": 448,
        "code": "fckyy",
        "name": "妇产科用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367041000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 21,
        "childs": "",
        "questionNumber": 200
    }, {
        "id": 449,
        "code": "gkyy",
        "name": "骨科用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367047000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 61,
        "childs": "",
        "questionNumber": 150
    }, {
        "id": 450,
        "code": "hxxtyy",
        "name": "呼吸系统用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367089000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 4,
        "childs": "",
        "questionNumber": 321
    }, {
        "id": 451,
        "code": "kgryw",
        "name": "抗感染药物",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367098000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 8,
        "childs": "",
        "questionNumber": 185
    }, {
        "id": 459,
        "code": "kzlyw",
        "name": "抗肿瘤药物",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367264000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 10,
        "childs": "",
        "questionNumber": 281
    }, {
        "id": 452,
        "code": "111",
        "name": "慢病用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367105000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 131,
        "childs": "",
        "questionNumber": 555
    }, {
        "id": 453,
        "code": "nfmxtyy",
        "name": "内分泌系统用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367169000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 7,
        "childs": "",
        "questionNumber": 395
    }, {
        "id": 454,
        "code": "555",
        "name": "肾内科",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367178000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 132,
        "childs": "",
        "questionNumber": 295
    }, {
        "id": 455,
        "code": "xhxtyy",
        "name": "消化系统用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367186000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 5,
        "childs": "",
        "questionNumber": 592
    }, {
        "id": 456,
        "code": "xxgyy",
        "name": "心血管系统用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367196000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 3,
        "childs": "",
        "questionNumber": 380
    }, {
        "id": 457,
        "code": "xyxtyy",
        "name": "血液系统用药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367214000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 59,
        "childs": "",
        "questionNumber": 185
    }, {
        "id": 458,
        "code": "zty",
        "name": "镇痛药",
        "olevel": 0,
        "pid": 0,
        "type": 2,
        "describe": "",
        "disabled": 0,
        "createTime": 1575367220000,
        "createUser": "",
        "updateTime": "",
        "updateUser": "",
        "deleteFlag": 0,
        "questionBankId": 31,
        "order": 0,
        "nameOriginId": 1,
        "childs": "",
        "questionNumber": 192
    }]


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


def get_one_exam_question_list(temp_headers, message, one_exam_id):
    # "https://www.yxgj.net/rest/exampaperresult/result/2081574"
    #                  question_result
    one_exam_id_url = 'https://www.yxgj.net/rest/exampaperresult/result/' + str(one_exam_id)
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
        print('获取考试试题列表失败')
        print(one_exam_question_list.status_code)


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


def cut_one_question(one_question_str):
    # 将str 转为 dict （json）
    one_question_ = json.loads(one_question_str)
    question_cut = {}
    # 题目信息筛选
    question_cut["id"] = one_question_["id"]
    question_cut["questionBankId"] = one_question_["questionBankId"]
    question_cut["title"] = one_question_["title"]
    question_cut["selectItem"] = one_question_["selectItem"]
    return question_cut


def save_questions(question_list_new, category_id_1_1):
    #
    # 存取问题
    #
    with open("question_result\question_" + str(category_id_1_1) + ".json", encoding='utf-8') as fca:
        # 先读取旧的信息
        question_list_old = json.load(fca, strict=False)
        print("旧的question_list_old长度=", len(question_list_old))
        fca.close()
        if (fca.closed):
            print("文件已关闭")
    # 与新的合并
    question_list_new = question_list_new + question_list_old
    print("题目：合并后的长度", len(question_list_new))

    # 在重新写入
    with open("question_result\question_" + str(category_id_1_1) + ".json", "w", encoding='utf-8') as fv:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(question_list_new, fv, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        fv.close()
        print(fv.closed)


def save_question_id(question_id_list_new, category_id_1_1):
    with open("question_result\question_id_" + str(category_id_1_1) + ".json", encoding='utf-8') as fc:
        # 先读取旧的信息
        question_id_list_old = json.load(fc, strict=False)
        print("旧的question_list_old长度=", len(question_id_list_old))
        fc.close()
        if (fc.closed):
            print("文件已关闭")
    # 新旧合并
    question_id_list_new = question_id_list_new + question_id_list_old
    print("id：合并后的长度=", len(question_id_list_new))
    # 去重
    # question_id_list_new_nr = list(set(question_id_list_new))
    # print("去重后的长度=", len(question_id_list_new_nr))
    # 按原顺序排序
    # question_id_list_new_r.sort(key=question_id_list_new.index)

    # 在重新写入
    with open("question_result\question_id_" + str(category_id_1_1) + ".json", "w", encoding='utf-8') as fv:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(question_id_list_new, fv, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        fv.close()
        print(fv.closed)


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


def create_file(category_id_1_1):
    #
    # 创建json文件存储数据
    #
    filename1 = "question_result\question_" + str(category_id_1_1) + ".json"
    file1 = [
        {
            "id": 88888,
            "questionBankId": 31,
            "selectItem": "[{\"answer\":0,\"text\":\"实例\",\"value\":0}, {\"answer\":0,\"text\":\"实例\",\"value\":1}, {\"answer\":0,\"text\":\"实例\",\"value\":2}, {\"answer\":1,\"text\":\"实例\",\"value\":3}]",
            "title": "实例"
        }
    ]
    if not os.path.isfile(filename1):  # 无文件时创建
        fd = open(filename1, mode="w", encoding="utf-8")
        fd.close()
    with open(filename1, "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(file1, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
    filename2 = "question_result\question_id_" + str(category_id_1_1) + ".json"
    file2 = [88888]
    if not os.path.isfile(filename2):  # 无文件时创建
        fd = open(filename2, mode="w", encoding="utf-8")
        fd.close()
    with open(filename2, "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(file2, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行


if __name__ == "__main__":
    ra = random.randint(0, 3)
    temp_headers = headers[ra]
    category_id_1_1 = 452
    # 登录获取session 和 用户id
    message = login.login("https://www.yxgj.net/rest/member/session")
    print("message")
    print(message)
    # 获取对应题目类型的题目数量
    question_number = get_question_number(temp_headers, message, category_id_1_1)
    print(question_number)

    # create_file(category_id_1_1)
    n = 2
    counter = 1
    while counter <= n:
        counter += 1
        # 获取一场考试的ID
        one_exam_id = get_one_exam_id(temp_headers, message, category_id_1_1)
        print(one_exam_id)
        # 通过考试ID获取该场考试的题目列表
        one_exam_question_list = get_one_exam_question_list(temp_headers, message, one_exam_id)
        print("初步获得的试题编号列表长度=", len(one_exam_question_list))
        print("初步获得的试题编号列表", one_exam_question_list)
        # 去除重复的问题ID
        one_exam_question_list_NO_Repeat = duplicate_detection(one_exam_question_list, category_id_1_1)
        print("去重后获得的试题编号列表长度=", len(one_exam_question_list))
        print("去重后获得的试题编号列表", one_exam_question_list)
        question_list = []
        question_id_list = []
        for one_question_id in one_exam_question_list_NO_Repeat:
            # 通过题目列表中的题目ID逐个获取　题目详细信息
            one_question = get_one_question(temp_headers, message, one_question_id)
            question_cut = cut_one_question(one_question)
            print(question_cut)
            question_list.append(question_cut)
            question_id_list.append(question_cut["id"])
        save_questions(question_list, category_id_1_1)
        save_question_id(question_id_list, category_id_1_1)
        print("添加问题", len(question_list), "个")
        print("添加问题ID", len(question_id_list), "个")
