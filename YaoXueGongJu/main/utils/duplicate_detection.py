import json

categort_id_1111 = 449
category_name = "骨科用药"
que_number = 119
with open("..\question_result\question_" + str(categort_id_1111) + ".json", encoding='utf-8') as fa:
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
print("类型嗷嗷阿",type(question_list_noRepeat))
# 在重新写入
with open("..\question_result\question_" +
          str(categort_id_1111) + "_" +
          str(category_name) + "_" +
          str(que_number) +
          ".json", "w",
          encoding='utf-8') as fvc:
    # json.dump(dict_var, f)  # 写为一行
    json.dump(question_list_noRepeat, fvc, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
    fvc.close()
    print(fvc.closed)
