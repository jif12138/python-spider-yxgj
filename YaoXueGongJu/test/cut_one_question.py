import json


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
