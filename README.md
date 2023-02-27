# Water Use Pipeline

### <ins> Team Members </ins>

Mackenzie Carter: mcarter1@sandiego.edu

Bryan Flores: bryanflores@sandiego.edu 

Caleb McCurdy: calebmccurdy@sandiego.edu

### <ins> Overview </ins>

An ELT pipeline related to water quality in California using data from the USGS API. Sourced from the United States Geological Survey water data services, the aim of this pipeline is to combine daily data from three main water conditions to provide an easy-access water quality data store. 

### <ins> Data Source </ins>

[USGS Middle River Location Monitoring](https://waterdata.usgs.gov/monitoring-location/11312676/)

### <ins> How to Deploy </ins>
Airflow Deployment: 
Installation of Airflow can be done easily using the Astro client found [here](https://github.com/astronomer/astro-cli)

Spiders must be placed as .py files into the 'include' folder of the Airflow directory, and any neccessary packages must be included in the requirements file. Examples are given in this repository. 

DAG files are used in airflow to deploy the pipeline on a daily timeframe. 


### <ins> How to Monitor </ins>
Monitoring of the pipeline can be done direcly in the Airflow webserver. 
