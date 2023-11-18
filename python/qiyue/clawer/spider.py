import re
import pandas as pd
import time
import pymongo

from urllib import request


class Spider():
    url_list = [r'https://www.xiangha.com/caipu/c-jiachang/hot-{}/'.format(i) for i in range(1, 4)]
    root_pattern = r'<div class="ins">([\s\S]*?)</div>'
    title_pattern = r'<a title="([\s\S]*?)" href='
    mat_pattern = r'<p class="info">([\s\S]*?)</p><p class="info">'
    review_pattern = r'<p class="info"><span>([\s\S]*?)浏览'
    collect_pattern = r'浏览</span>([\s\S]*?)收藏'

    # def __fetch_content(self):
    #     r = request.urlopen(Spider.url)
    #     htmls = r.read()
    #     htmls = str(htmls, encoding='utf-8')
    #     return htmls

    def __analysis(self):
        anchors = []
        for url in Spider.url_list:
            r = request.urlopen(url)
            htmls = r.read()
            htmls = str(htmls, encoding='utf-8')
            root_html = re.findall(Spider.root_pattern, htmls)
            for html in root_html:
                title = re.findall(Spider.title_pattern, html)[0]
                mat = re.findall(Spider.mat_pattern, html)[0]
                review = re.findall(Spider.review_pattern, html)[0]
                collect = re.findall(Spider.collect_pattern, html)[0]
                anchor = {'title': title, 'mat': mat, 'review': int(review), 'collect': int(collect)}
                anchors.append(anchor)
            print(anchors)
            time.sleep(6)
        return anchors

    def __toDataframe(self, anchors):
        df = pd.DataFrame(anchors)
        print(df)
        return df
    # def __refine(self, anchors):
    #     l = lambda x:

    def __sort(self, anchors):
        anchors = sorted(anchors, key=lambda x:x["collect"],reverse=True)
        return anchors

    def __saveToMongoDB(self, anchors):
        client = pymongo.MongoClient('mongodb://{}:{}@39.98.59.77:27017/'.format("***", "***"))
        mydb = client["caipu"]
        mycol = mydb["jiachangcai"]
        mycol.insert_many(anchors)

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1) + ":" + anchors[rank]["title"]
                  + "-------" + str(anchors[rank]["collect"]))

    # def __sort_seed(self, anchor):
        # return anchor["collect"]

    def go(self):
        # htmls = self.__fetch_content()
        anchors = self.__analysis()
        anchors = self.__sort(anchors)
        self.__show(anchors)
        self.__toDataframe(anchors)
        self.__saveToMongoDB(anchors)
spider = Spider()
spider.go()
# print(dir())