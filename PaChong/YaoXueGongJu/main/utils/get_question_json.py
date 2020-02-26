import json


def get_question_bank_json():
    with open("..\json\question_bank.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
        print(f.closed)
    print(type(data))
    print(data)
    list1 = []
    for i in data:
        d = {"id": i["id"], "name": i["name"], "code": i["code"], "quantity": i["quantity"]}
        list1.append(d)
    print(list1)

    with open("..\json\question_bank_cut.json", "w", encoding='utf-8') as fc:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(list1, fc, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        fc.close()
        print(fc.closed)


def get_question_category_json():
    with open("..\json\question_category.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
        print(f.closed)
    print(type(data))
    print(data)
    list1 = []
    for i in data:
        d = {"id": i["id"], "name": i["name"], "code": i["code"], "questionBankId": i["questionBankId"],
             "nameOriginId": i["nameOriginId"], "questionNumber": i["questionNumber"]}
        list1.append(d)
    print(list1)

    with open("..\json\question_category_cut.json", "w", encoding='utf-8') as fc:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(list1, fc, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        f.close()
        print(f.closed)


if __name__ == "__main__":
    get_question_bank_json();
    # get_question_category_json();
# def get_question_
