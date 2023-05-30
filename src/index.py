import datetime

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *


from pyspark.conf import SparkConf
from pyspark.context import SparkContext
conf = SparkConf()
conf.setMaster("local").setAppName("My app")

sc = SparkContext(conf=conf)
spark_session = SparkSession(sc)


def createMyDataFrame():
    dataframe = spark_session.createDataFrame(
        data = [
            [datetime.date(2020, 1, 1), 'demo', 1.123, 10],
            [None, None, None, None],
        ],
        schema=StructType(
            [
                StructField('col_a', DateType(), True),
                StructField('col_b', StringType(), True),
                StructField('col_c', DoubleType(), True),
                StructField('col_d', LongType(), True),
            ]
        ),
    )

    dataframe.show()
    return dataframe

