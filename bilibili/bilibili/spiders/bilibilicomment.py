import scrapy
from urllib.parse import urlencode
from bilibili.items import BilibiliItem


class BilibilicommentSpider(scrapy.Spider):
    name = 'bilibilicomment'
    allowed_domains = ['api.bilibili.com']
    api_url = 'https://api.bilibili.com/pgc/review/short/list?'
    params = {
        'media_id': '28237119',
        'ps': '20',
        'sort': '0',
    }
    start_urls = [api_url + urlencode(params)]

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
