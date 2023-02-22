from pathlib import Path
# from spiders.middleriver_urls import *
import scrapy
import datetime

current_time = datetime.datetime.now().isoformat()

week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
week_ago_iso = week_ago.isoformat()

mr_nitrates = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=99133&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

mr_ph = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=00400&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

mr_salinity = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=00480&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

class WaterSpider(scrapy.Spider):
    name = "middleriver"

    def start_requests(self):
        urls = [
            mr_nitrates,
            mr_ph,
            mr_salinity
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("&")[1].split("=")[1]
        filename = f'middleriver-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
        
