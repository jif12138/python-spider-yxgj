import os
import json


def createFile(category_id_1_1):
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
