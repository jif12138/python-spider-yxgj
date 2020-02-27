import requests
from requests.exceptions import RequestException
import re


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        # response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        return RequestException.errno


def parse_one_page(html):
    pattern = re.compile('<dd>')


def main():
    # url = 'https://www.maoyan.com/board/4/'
    # url = 'https://www.yxgj.net/#exam-paper/result/2075370'
    url= 'https://www.yxgj.net/rest/question/37274?examPaperResultId=2076857'
    html = get_one_page(url)

    print(html)


if __name__ == '__main__':
    main()
