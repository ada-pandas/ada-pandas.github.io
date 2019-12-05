# -*- coding: utf-8 -*-

import pyspark
from pyspark import SparkContext, SQLContext
from pyspark.sql import *
conf = pyspark.SparkConf().setAll([("spark.executor.instances", 4),
                                    ('spark.executor.cores', 8),
                                   ('spark.executor.memory', '12g'),
                                   ('spark.driver.memory','12g'),
                                   ('spark.driver.maxResultSize', '4G')
                                  ])
# context initialization
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sc = spark.sparkContext

from pyspark.sql.types import *
from pyspark.sql.functions import year, month, dayofmonth, avg, first

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
    .csv('./data/*/CO/*', schema=schema, header=True) \
    .drop("Namespace", "AirQualityStation", "AirQualityNetwork", "SamplingPoint", "SamplingProcess", "Sample", "AirPollutantCode")

unrel_stations = df.select("EoICode").where((df.Concentration > 100) & (df.Unit == "mg/m3")).distinct()

is_valid = (df.Validity > 0) & (df.Verification < 3)
is_dangerous = (df.Concentration >= 7.5) & (df.Unit == "mg/m3") \
               | (df.Concentration >= 7500) & (df.Unit == u"µg/m3")

df.join(unrel_stations, "EoICode", how='left_anti').select("*").where(is_valid & is_dangerous) \
    .write.csv('CO-Medium', timestampFormat="yyyy-MM-dd hh:mm:ss")