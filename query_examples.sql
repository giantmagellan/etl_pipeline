use water_quality;

# Nitrate levels where collection @ Sacramento River results in less than 0.4 mg per liter
SELECT
	collection_datetime,
    nitrate_level
FROM sacriver
WHERE nitrate_level < 0.4;

# Datetime and pH where collection @ Ryer Island results in a pH value of at least 8
SELECT
	collection_datetime,
    pH_value
FROM ryerisland
WHERE pH_value >= 8;

# Salinity and nitrate levels @ Sacramento River during 11 o'clock hour
SELECT
    collection_datetime,
    salinity_level,
    nitrate_level
FROM sacriver
WHERE collection_datetime LIKE '%11:%';
