import datetime

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *

from pyspark_test import assert_pyspark_df_equal
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
conf = SparkConf()
conf.setMaster("local").setAppName("My app")

sc = SparkContext(conf=conf)
spark_session = SparkSession(sc)

df_1 = spark_session.createDataFrame(
    data=[
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

df_2 = spark_session.createDataFrame(
    data=[
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
df_1.show()
assert_pyspark_df_equal(df_1, df_2)