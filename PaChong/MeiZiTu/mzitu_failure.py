import requests  ##导入requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os
from lxml import etree


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mzitu.com/all'
##开始的URL地址
start_html = requests.get(all_url,  headers=headers)
##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
print(start_html.text)
##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)


Soup = BeautifulSoup(start_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
#li_list = Soup.find_all('li') ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
#for li in li_list: ##这个不解释了。看不懂的效小哥儿回去瞅瞅基础教程
    #print(li) ##同上
all_a = Soup.find('div', class_='all').find_all('a')[1:] ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
for a in all_a:
    title = a.get_text()  # 取出a标签的文本
    href = a['href']  # 取出a标签的href 属性
    html = requests.get(href, headers=headers)  ##上面说过了
    html_Soup = BeautifulSoup(html.text, 'lxml')  ##上面说过了
    # print(href)
    # print(html_Soup.find('div', class_='pagenavi'))
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    for page in range(1, int(max_span) + 1):  ##不知道为什么这么用的小哥儿去看看基础教程吧
        page_url = href + '/' + str(page)  ##同上
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']  ##这三行上面都说过啦不解释了哦
        name = img_url[-9:-4]  ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url, headers=headers)
        f = open(name + '.jpg', 'ab')  ##写入多媒体文件必须要 b    这个参数！！必须要！！
        f.write(img.content)  ##多媒体文件要是用conctent哦！
        f.close()
        # print(page_url)

##    find’ 只查找给定的标签一次，就算后面还有一样的标签也不会提取出来哦！ 而  ‘find_all’ 是在页面中找出所有给定的标签！有十个给定的标签就返回十个



