import json

category_list = [
    {
        "id": 447,
        "name": "儿科用药",
        "questionNumber": 167
    },
    {
        "id": 448,
        "name": "妇产科用药",
        "questionNumber": 152
    },
    {
        "id": 449,
        "name": "骨科用药",
        "questionNumber": 119
    },
    {
        "id": 450,
        "name": "呼吸系统用药",
        "questionNumber": 265
    },
    {
        "id": 451,
        "name": "抗感染药物",
        "questionNumber": 165
    },
    {
        "id": 459,
        "name": "抗肿瘤药物",
        "questionNumber": 241
    },
    {
        "id": 452,
        "name": "慢病用药",
        "questionNumber": 470
    }]


# 题目list去重
def duplicate_detection(categort_id_1111, category_name, que_number):
    duplicate_detection_url = "..\question_result\question_" + \
                              str(categort_id_1111) + ".json"
    with open(duplicate_detection_url, encoding='utf-8') as fa:
        question_list_old = json.load(fa)
        fa.close()
    print(type(question_list_old))
    print(len(question_list_old))

    # 去除结果集中重复的元素
    question_list_noRepeat = []
    question_id_list = []
    question_id_list_noRepeat = []
    for oneQuestion in question_list_old:
        question_id_list.append(oneQuestion["id"])
    print("结果中原共有", len(question_id_list), "道题目")
    # print(question_id_list)
    question_id_list_noRepeat = list(set(question_id_list))
    question_id_list_noRepeat.sort(key=None, reverse=False)
    print("去重后，共有", len(question_id_list_noRepeat), "道题目")
    # print(question_id_list_noRepeat)
    # 获取全部题目的ID 生成list
    for oneQuestion2 in question_list_old:

        if oneQuestion2["id"] in question_id_list_noRepeat:
            question_id_list_noRepeat.remove(oneQuestion2["id"])
            print(oneQuestion2["id"], "已加入新结果中")
            question_list_noRepeat.append(oneQuestion2)
        else:
            print(oneQuestion2["id"], "重复，放弃")

    print("题目数量", len(question_list_noRepeat))
    no_repeat_url = "..\question_result\question_" + \
                    str(categort_id_1111) + "_" + \
                    str(category_name) + "_" + \
                    str(que_number) + "_noRepeat.json"
    # 在重新写入
    with open(no_repeat_url, "w", encoding='utf-8') as fvc:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(question_list_noRepeat, fvc, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        fvc.close()
        print(fvc.closed)
    print(len(question_list_noRepeat), "道题目已存入", no_repeat_url)


# 题目json 转 txt存储
def json2txt(categort_id_1111, category_name, que_number):
    print("读取题目文件。。。")
    json2txt_open_file_url = "..\question_result\question_" + \
                             str(categort_id_1111) + "_" + \
                             str(category_name) + "_" + \
                             str(que_number) + "_noRepeat.json"
    with open(json2txt_open_file_url, encoding='utf-8') as fa:
        question_list_ = json.load(fa)
        fa.close()
    print("成功读取题目", json2txt_open_file_url, "文件，文件关闭！")
    que_dict = {}
    que_list = []
    print("格式化题目中。。。")
    count = 1
    for oneQuestion in question_list_:
        # 选项
        oneQuestion_selectItem = json.loads(oneQuestion["selectItem"])
        selectItem_str = "A、" + str(oneQuestion_selectItem[0]["text"]) + \
                         " B、" + str(oneQuestion_selectItem[1]["text"]) + \
                         "C、" + str(oneQuestion_selectItem[2]["text"]) + \
                         "D、" + str(oneQuestion_selectItem[3]["text"])
        if len(oneQuestion_selectItem) == 5:
            selectItem_str = selectItem_str + "E、" + str(oneQuestion_selectItem[4]["text"])

        # 答案
        answer_list = []
        for selectItem in oneQuestion_selectItem:
            if selectItem["answer"] == 1:
                if selectItem["value"] == 0:
                    answer_list.append("A、")
                elif selectItem["value"] == 1:
                    answer_list.append("B、")
                elif selectItem["value"] == 2:
                    answer_list.append("C、")
                elif selectItem["value"] == 3:
                    answer_list.append("D、")
                elif selectItem["value"] == 4:
                    answer_list.append("E、")
                else:
                    print("答案组装出错")

        # 题目
        title = oneQuestion["title"] + "(" + ''.join(answer_list) + ")"
        # print(count, "、题目：", title)
        # print("选项：", selectItem_str)
        que_dict = {"题目：": title, "选项：": selectItem_str}
        que_list.append(que_dict)
        count += 1
        json2txt_write_file_url = "..\question_result\question_" + \
                                  str(categort_id_1111) + "_" + \
                                  str(category_name) + "_" + \
                                  str(que_number) + ".txt"

        # 写入txt文档
        file_object = open(json2txt_write_file_url, mode='a', encoding='utf-8')
        file_object.write(str(count) + "、题目：" + title + "\n" + "选项：" + selectItem_str + "\n")
    print("格式化题目完成共发现", len(que_list), "道题目！")
    print("写入文件")
    print(type(que_list))


if "__main__" == __name__:

    for one_category in category_list:
        categort_id_1111 = one_category["id"]
        category_name = one_category["name"]
        que_number = one_category["questionNumber"]

        duplicate_detection(categort_id_1111, category_name, que_number)
        json2txt(categort_id_1111, category_name, que_number)
