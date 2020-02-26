import json


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
