from pathlib import Path
from datetime import date, timedelta
import pandas as pd

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
        param_codes = ['99133', '00400', '00480']  # nitrates, pH, salinity
        end_date = date.today()
        start_date = end_date - timedelta(days=7)

        urls = [         
                'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd={}&startDT={}&endDT={}&siteStatus=all&format=rdb'.format(param_codes[0], start_date, end_date),
                'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd={}&startDT={}&endDT={}&siteStatus=all&format=rdb'.format(param_codes[1], start_date, end_date),
                'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd={}&startDT={}&endDT={}&siteStatus=all&format=rdb'.format(param_codes[2], start_date, end_date)

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("parameterCd=")[-1].split("&")[0]
        filename = f'middleriver-{page}.tsv'
        # csv_table = pd.read_table(filename, sep="\t").to_csv(f'middleriver-{page}.csv', index=False)
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
        
