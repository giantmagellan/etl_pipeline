# USGS SITE: CACHE SLOUGH AB RYER ISLAND FERRY NR RIO VISTA CA
# SITE NO.: 11455385

from pathlib import Path
from datetime import date, timedelta
import pandas as pd

import scrapy

class WaterSpider(scrapy.Spider):
    name = "ryerisland"

    def start_requests(self):
        url_init = "https://waterservices.usgs.gov/nwis/iv/?sites="
        url_end = "&siteStatus=all&format=rdb"
        monitor_loc = "11455385"
        param_codes = ['99133', '00400', '00480']  # nitrates, pH, salinity
        end_date = date.today()
        past_week = end_date - timedelta(days=7)  # obtain data for the past 7 days
        start_date = end_date - timedelta(days=1) # obtain data from the past day

        if past_week == end_date:
            urls = ['{}{}&parameterCd={}&startDT={}&endDT={}{}'.format(url_init, monitor_loc, code, past_week, end_date, url_end) for code in param_codes]
        else:
            urls = ['{}{}&parameterCd={}&startDT={}&endDT={}{}'.format(url_init, monitor_loc, code, start_date, end_date, url_end) for code in param_codes]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("parameterCd=")[-1].split("&")[0]
        filename = f'waterpipeline/data_samples/ryerisland-{page}.tsv'
        # csv = pd.read_table(filename, sep="\t", skiprows=26)
        # csv = csv.to_csv(f'waterpipeline/data_samples/ryerisland-{page}.csv', index=False)
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
        
