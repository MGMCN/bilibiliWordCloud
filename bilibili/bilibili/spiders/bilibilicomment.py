import scrapy
from urllib.parse import urlencode
from bilibili.items import BilibiliItem
from dotenv import load_dotenv
import os


class BilibilicommentSpider(scrapy.Spider):
    name = 'bilibilicomment'
    allowed_domains = ['api.bilibili.com']
    api_url = 'https://api.bilibili.com/pgc/review/short/list?'

    def __init__(self, *args, **kwargs):
        load_dotenv()
        media_id = os.getenv('media_id')
        super(BilibilicommentSpider, self).__init__(*args, **kwargs)
        self.params = {
            'media_id': media_id,
            'ps': '20',
            'sort': '0',
        }
        self.start_urls = [self.api_url + urlencode(self.params)]

    def parse(self, response):
        json = response.json()
        if json:
            datas = json.get('data')
            items = datas.get('list', {})
            next = datas.get('next')
            if next:
                self.params['cursor'] = str(next)
                next_url = self.api_url + urlencode(self.params)
                yield scrapy.Request(url=next_url, callback=self.parse)
            if items:
                if len(items) > 0:
                    for item in items:
                        bilibiliitem = BilibiliItem()
                        bilibiliitem['comment'] = item.get('content')
                        yield bilibiliitem
