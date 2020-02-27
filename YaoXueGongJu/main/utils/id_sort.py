import json


def id_sort():
    with open("..\question_result\question_id.json", "r", encoding='utf-8') as fc:
        data = json.load(fc)
        print(type(data))
        print("排序前：", data)
        data.sort(key=None, reverse=False)
        print("排序后：", data)
        print("文件关闭:", fc.closed)
    with open("..\question_result\question_id_sort.json", "w", encoding='utf-8') as fv:
        json.dump(data, fv, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
        print("文件关闭:", fv.closed)


def duplicate_detection():
    with open("..\question_result\question_id.json", encoding="utf-8") as f:
        data = json.load(f)
        f.close()
        print(f.closed)
        print(type(data))
        print(data)


if __name__ == "__main__":
    id_sort()
