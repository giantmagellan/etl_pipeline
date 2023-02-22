from pathlib import Path
from datetime import date, timedelta
import pandas as pd

import scrapy

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
        
