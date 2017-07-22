# -*- coding: utf-8 -*-
# @File    : 爬虫练习
# @Author  : Matthew Liu

import requests
from bs4 import BeautifulSoup
import time


# Try1 爬取贴吧
tieba_url = 'http://tieba.baidu.com/f?kw=%E5%90%89%E6%9E%97%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=0'
tieba_urls = ['http://tieba.baidu.com/f?kw=%E5%90%89%E6%9E%97%E5%A4%A7%E5%AD%A6&ie=utf-8&pn={0}'.format(str(i)) for i in range(0,200,50)]

def bbs_crawler_single_page(url):
    bbs_data = requests.get(url)
    soup = BeautifulSoup(bbs_data.text,'lxml')
    titles = soup.select('  li.j_thread_list.clearfix > div > div.col2_right.j_threadlist_li_right > div.threadlist_lz.clearfix > div.threadlist_title.pull_left.j_th_tit > a')
    auswers = soup.select(' li.j_thread_list.clearfix > div > div.col2_left.j_threadlist_li_left > span')
    contents  = soup.select(' li.j_thread_list.clearfix > div > div.col2_right.j_threadlist_li_right > div.threadlist_detail.clearfix > div.threadlist_text.pull_left > div.threadlist_abs.threadlist_abs_onlyline')

    # 去除置顶的
    for i in range(len(titles)-len(contents)):
        titles.pop(0)
        auswers.pop(0)

    sigle_page = []
    for title,answer,content in zip(titles,auswers,contents):
        info = {
            'title':title.get_text(),
            'answer':answer.get_text(),
            'content':content.get_text()
        }
        # print(info)
        sigle_page.append(info)
    time.sleep(2)
    return sigle_page


def bbs_crawler(page_urls):
    pages = []
    for url in page_urls:
        single_page = bbs_crawler_single_page(url)
        print('page ',url)
        pages.append(single_page)
        print(single_page)
        print("++++++++++++++++")

    return  pages




if __name__ == '__main__':
    bbs_crawler(tieba_urls)
