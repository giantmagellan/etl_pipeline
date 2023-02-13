from pathlib import Path
from middleriver_urls import *

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "middleriver"

    def start_requests(self):
        urls = [
            mr_nitrates
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url
        filename = f'middleriver-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {mr_nitrates.txt}')