from pathlib import Path
#from spiders.sacramentoriver_urls import *
import scrapy
import datetime

current_time = datetime.datetime.now().isoformat()

week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
week_ago_iso = week_ago.isoformat()

sr_nitrates = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=99133&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'
sr_ph = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00400&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'
sr_salinity = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00480&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

class WaterSpider(scrapy.Spider):
    name = "sacramentoriver"

    def start_requests(self):
        urls = [
            sr_nitrates,
            #'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=99133&startDT=2023-02-09T13:26:39.886-08:00&endDT=2023-02-16T13:26:39.886-08:00&siteStatus=all&format=rdb',
            sr_ph,
            #'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00400&startDT=2023-02-09T13:25:01.674-08:00&endDT=2023-02-16T13:25:01.674-08:00&siteStatus=all&format=rdb'
            sr_salinity,
            #'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00480&startDT=2023-02-09T13:33:20.613-08:00&endDT=2023-02-16T13:33:20.613-08:00&siteStatus=all&format=rdb',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("parameterCd=")[-1].split("&")[0]
        filename = f'waterpipeline/data_samples/ryerisland-{page}.csv'
        data = response.body.decode("utf-8")  
        csv = pd.read_csv(io.StringIO(data), sep="\t", skiprows=26)
        csv = csv.to_csv(filename, index=False)
        Path(csv).write_bytes(response.body)
        self.log(f'Saved file {csv}')
