# USGS SITE: CACHE SLOUGH AB RYER ISLAND FERRY NR RIO VISTA CA
# SITE NO.: 11455385

from pathlib import Path
from datetime import date, datetime, time, timedelta
import pandas as pd
import io
import scrapy

# Datetime Elements
today = date.today()
start_date = today - timedelta(days=1)  # obtain data from the past day
start_short = start_date.strftime("%Y%m%d")  # start date in short format for csv output
start_dt_iso = datetime.combine(start_date, time.min).isoformat()
end_dt_iso = datetime.combine(start_date, time.max).isoformat()

class WaterSpider(scrapy.Spider):
    name = "ryerisland"

    def start_requests(self):
        url_init = "https://waterservices.usgs.gov/nwis/iv/?sites="
        url_end = "&siteStatus=all&format=rdb"
        monitor_loc = "11455385"
        param_codes = ['99133', '00400', '00480']  # nitrates, pH, salinity

        urls = ['{}{}&parameterCd={}&startDT={}&endDT={}{}'.format(url_init, monitor_loc, code, start_dt_iso, end_dt_iso, url_end) for code in param_codes]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("parameterCd=")[-1].split("&")[0]
        filename = f'waterpipeline/data_samples/ryerisland-{page}-{start_short}.csv'
        data = response.body.decode("utf-8")  
        csv = pd.read_csv(io.StringIO(data), sep="\t", skiprows=26)
        csv = csv.to_csv(filename, index=False)
        Path(csv).write_bytes(data)
        self.log(f'Saved file {csv}')