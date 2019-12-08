# -*- coding: utf-8 -*-

import pyspark
from pyspark import SparkContext, SQLContext
from pyspark.sql import *

conf = pyspark.SparkConf().setAll([("spark.executor.instances", 4),
                                   ('spark.executor.cores', 8),
                                   ('spark.executor.memory', '12g'),
                                   ('spark.driver.memory', '12g'),
                                   ('spark.driver.maxResultSize', '4G')
                                   ])
# context initialization
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext

from pyspark.sql.types import *
from pyspark.sql.functions import year, month, dayofmonth, avg, first, when

schema = StructType([StructField('Country', StringType(), True),
                     StructField('Namespace', StringType(), True),
                     StructField('AirQualityNetwork', StringType(), True),
                     StructField('AirQualityStation', StringType(), True),
                     StructField('EoICode', StringType(), True),
                     StructField('SamplingPoint', StringType(), True),
                     StructField('SamplingProcess', StringType(), True),
                     StructField('Sample', StringType(), True),
                     StructField('Pollutant', StringType(), True),
                     StructField('AirPollutantCode', StringType(), True),
                     StructField('AveragingTime', StringType(), True),
                     StructField('Concentration', FloatType(), True),
                     StructField('Unit', StringType(), True),
                     StructField('DatetimeBegin', TimestampType(), True),
                     StructField('DatetimeEnd', TimestampType(), True),
                     StructField('Validity', IntegerType(), True),
                     StructField('Verification', IntegerType(), True)])

df = spark.read.format("com.databricks.spark.csv").option("inferSchema", "true") \
    .option("timestampFormat", "yyyy-MM-dd hh:mm:ss XXX") \
    .csv('./data/*/*/*', schema=schema, header=True, mode="DROPMALFORMED") \
    .drop("Namespace", "AirQualityStation", "AirQualityNetwork", "SamplingPoint", "SamplingProcess", "Sample",
          "AirPollutantCode")

pollutants = ["CO", "NO2", "O3", "SO2", "PM10", "PM2.5"]
is_valid = (df.Validity > 0) & (df.Verification < 3) & (df.Concentration > 0) & (df.Pollutant.isin(pollutants))

df.where(is_valid).groupBy(["Country", "Pollutant", year("DatetimeBegin").alias("Year"),
                            month("DatetimeBegin").alias("Month")]) \
    .agg(avg(when((df.Unit == u"µg/m3") | (df.Unit == "mg/l"), df.Concentration) \
             .when(df.Unit == "mg/m3", df.Concentration * 1000) \
             .when(df.Unit == "ng/m3", df.Concentration / 1000) \
             .otherwise(None)).alias("Avg (µg/m3)")) \
    .sort(["Country", "Pollutant", "Year", "Month"]) \
    .write.csv('kekz', timestampFormat="yyyy-MM-dd hh:mm:ss")
