# USGS SITE: SACRAMENTO R AB DELTA CROSS CHANNEL CA 
# SITE NO.: 11447890

from pathlib import Path
from datetime import date, timedelta
import pandas as pd
import io

import scrapy

class WaterSpider(scrapy.Spider):
    name = "sacramentoriver"

    def start_requests(self):
        url_init = "https://waterservices.usgs.gov/nwis/iv/?sites="
        url_end = "&siteStatus=all&format=rdb"
        monitor_loc = "11447890"
        param_codes = ['99133', '00400', '00480']  # nitrates, pH, salinity
        end_date = date.today()
        week_ago = end_date - timedelta(days=7)  # obtain data for the past 7 days
        start_date = end_date - timedelta(days=1) # obtain data from the past day

        if week_ago == end_date:
            urls = ['{}{}&parameterCd={}&startDT={}&endDT={}{}'.format(url_init, monitor_loc, code, week_ago, end_date, url_end) for code in param_codes]
        else:
            urls = ['{}{}&parameterCd={}&startDT={}&endDT={}{}'.format(url_init, monitor_loc, code, start_date, end_date, url_end) for code in param_codes]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("parameterCd=")[-1].split("&")[0]
        filename = f'waterpipeline/data_samples/sacramentoriver-{page}.csv'
        data = response.body.decode("utf-8")  
        csv = pd.read_csv(io.StringIO(data), sep="\t", skiprows=26)
        csv = csv.to_csv(filename, index=False)
        Path(csv).write_bytes(data)
        self.log(f'Saved file {csv}')