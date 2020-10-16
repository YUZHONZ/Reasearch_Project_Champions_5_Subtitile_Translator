import requests
import urllib3.request
from bs4 import BeautifulSoup
from lxml import etree
import csv
import pandas as pd

headers = {
            'User-Agent':''
            }

class YyeTs:
    def __init__(self,url):
        self.url=url

    def list_page(self):
        for page_num in range(117,151):
            self.url = 'http://www.zimuku.la/t/HJns0?p=' + str(page_num)
            # print(self.url)
            print('Page{}'.format(str(page_num)))

            response = requests.get(self.url,headers=headers,timeout=20)
            print(response.status_code)
            self.get_per_page(response.text)

    def get_per_page(self,one_page_data):
        # html = etree.HTML(response.text)
        html = etree.HTML(one_page_data)

        details = html.xpath("//tr[@class='odd' or 'even']//td[@class='first']")


        subs = []
        name = []
        urls = []
        for label in details:
            first_class=label.xpath(".//span/text()")
            if 'SRT' in first_class:
                # print(first_class)
                pass

        if first_class[0] == 'SRT':
            names = label.xpath("//a//@title")
            for all_names in names:
                if '【YYeTs字幕组 简繁英双语字幕】' in all_names:
                    name.append(all_names)
                    # print(all_names)
            all_urls=label.xpath("//a/@href")
            for detail_url in all_urls:
                if 'detail' in detail_url:
                    # print('http://www.zimuku.la'+detail_url)
                    all_sites = 'http://www.zimuku.la' + detail_url
                    # print(all_sites)
                    self.detail_page(all_sites)
                    # urls.append(all_sites)

        # #
        # comb = zip(name,urls)
        # combDic=dict((name,urls)for name,urls in comb)
        # # print(combDic)
        # keys=combDic.keys()
        # for key in keys:
        #     value=combDic[key]
        #     print('%s:%s'%(key,value))
        #     subs.append('%s:%s'%(key,value))
        #         # self.detail_page(urls)
        #         # return urls

        # print("next step2")

        # self.detail_page(all_sites)

    def detail_page(self,use_urls):
        responses = requests.get(url=use_urls, headers=headers, timeout=20)
        # print(responses.status_code)
        # print(responses.text)
        html = etree.HTML(responses.text)
        details = html.xpath("//li[@class='li dlsub']//a/@href")
        # print(details)
        for down_1 in details:
            if 'zmk.pw' in down_1:
                pass
                print(down_1)
                self.downpage(down_1)

    def downpage(self,downsite):
        responses = requests.get(url=downsite, headers=headers, timeout=20)
        # print(responses.status_code)
        html = etree.HTML(responses.text)
        downpage = html.xpath("//ul/li//a/@href")[0]
        downsites = 'http://zmk.pw' + downpage
        # print(downsites)
        # for donw_2 in downpage:
        #     if 'dx1' in downpage:
        #         print(downsites)
        #     pass


if __name__ == '__main__':
    url ='http://www.zimuku.la/t/HJns0?p='
    subs=YyeTs(url)
    subs.list_page()