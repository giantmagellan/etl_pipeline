
current_time = datetime.datetime.now().isoformat()

<<<<<<< HEAD
mr_salinity = 'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=00480&startDT=2023-01-29T13:18:33.327-08:00&endDT=2023-02-05T13:18:33.327-08:00&siteStatus=all&format=rdb'

mr_parent = 'https://waterdata.usgs.gov/monitoring-location/11312676/#parameterCode=00065&period=P7D'

mr_nitrate_dummy = 'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=99133&startDT=2023-02-10T00:00:00.000-08:00&endDT=2023-02-13T00:00:00.000-08:00&siteStatus=all&format=rdb'
=======
week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
week_ago_iso = week_ago.isoformat()

#print("Current time (ISO 8601 format):", current_time)
#print("One week ago (ISO 8601 format):", week_ago)
#print("One week ago:", week_ago_iso)


mr_nitrates = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=99133&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

mr_ph = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=00400&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'

mr_salinity = f'https://waterservices.usgs.gov/nwis/iv/?sites=11312676&parameterCd=00480&startDT={week_ago_iso}&endDT={current_time}&siteStatus=all&format=rdb'
>>>>>>> 73edc55cc692913302ed21c8f357178943e8beb3
