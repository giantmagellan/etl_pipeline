use water_quality;

#select * from sac_ph;

ALTER TABLE sac_ph 
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN pH_value float,
MODIFY COLUMN data_value CHAR(1);

#select * from sac_salinity;

ALTER TABLE sac_salinity
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN salinity_level float,
MODIFY COLUMN data_value CHAR(1);

# select * from sac_nitrates;
ALTER TABLE sac_nitrates
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN nitrate_level float,
MODIFY COLUMN data_value CHAR(1);




#select * from ryer_ph;

ALTER TABLE ryer_ph 
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN pH_value float,
MODIFY COLUMN data_value CHAR(1);

#select * from ryer_salinity;

ALTER TABLE ryer_salinity
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN salinity_level float,
MODIFY COLUMN data_value CHAR(1);

#select * from ryer_nitrates;

ALTER TABLE ryer_nitrates
MODIFY COLUMN agency_cd VARCHAR(10),
MODIFY COLUMN time_zone VARCHAR(10),
MODIFY COLUMN nitrate_level float,
MODIFY COLUMN data_value CHAR(1);