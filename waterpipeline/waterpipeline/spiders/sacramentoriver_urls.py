current_time = datetime.datetime.now().isoformat()

week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
week_ago_iso = week_ago.isoformat()

#print("Current time (ISO 8601 format):", current_time)
#print("One week ago (ISO 8601 format):", week_ago)
#print("One week ago:", week_ago_iso)



sr_nitrates = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=99133&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

sr_ph = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00400&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

sr_salinity = f'https://waterservices.usgs.gov/nwis/iv/?sites=11447890&parameterCd=00480&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'
