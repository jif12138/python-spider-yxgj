import json


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
