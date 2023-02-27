use water_quality;

DROP VIEW sacriver;

CREATE VIEW sacriver AS
SELECT 
	sp.collection_date as collection_datetime, 
	sp.time_zone, 
    sp.ph_value,
    CASE
		WHEN pH_value >= 7.5 THEN 'high'
        WHEN pH_value >= 6.5 AND pH_value < 7.5 THEN 'medium'
        ELSE 'low'
	END AS pH_label,
    ss.salinity_level,
    sn.nitrate_level
FROM sac_ph sp
INNER JOIN sac_salinity ss
ON sp.collection_date = ss.collection_date
INNER JOIN sac_nitrates sn
ON sp.collection_date = sn.collection_date;

SELECT * FROM sacriver;



DROP VIEW ryerisland;

CREATE VIEW ryerisland AS
SELECT 
	rp.collection_date as collection_datetime, 
	rp.time_zone, 
    rp.ph_value,
    CASE
		WHEN pH_value >= 7.5 THEN 'high'
        WHEN pH_value >= 6.5 AND pH_value < 7.5 THEN 'medium'
        ELSE 'low'
	END AS pH_label,
    rs.salinity_level,
    rn.nitrate_level
FROM ryer_ph rp
INNER JOIN ryer_salinity rs
ON rp.collection_date = rs.collection_date
INNER JOIN ryer_nitrates rn
ON rp.collection_date = rn.collection_date;

SELECT * FROM ryerisland;
