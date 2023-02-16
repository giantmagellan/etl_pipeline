from pathlib import Path
# from spiders.sacramentoriver_urls import *

import scrapy

class WaterSpider(scrapy.Spider):
    name = "sacramentoriver"

    def start_requests(self):
        urls = [
            # sr_nitrates
            'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=99133&startDT=2023-02-09T13:26:39.886-08:00&endDT=2023-02-16T13:26:39.886-08:00&siteStatus=all&format=rdb'
          
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'sacramentoriver-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
