from pathlib import Path
# from spiders.middleriver_urls import *

import scrapy

class WaterSpider(scrapy.Spider):
    name = "middleriver"

    def start_requests(self):
        urls = [
            # mr_nitrates
            'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=99133&startDT=2023-01-29T13:06:19.614-08:00&endDT=2023-02-05T13:06:19.614-08:00&siteStatus=all&format=rdb'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'middleriver-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')