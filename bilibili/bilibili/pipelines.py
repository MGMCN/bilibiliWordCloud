# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class BilibiliPipeline:
    def process_item(self, item, spider):
        os.system('echo ' + '\"' + item['comment'] + '\"' + '>>' + 'comments.txt')  # 为了方便就这么写了
        return item
