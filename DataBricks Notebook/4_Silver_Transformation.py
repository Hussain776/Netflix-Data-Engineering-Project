# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Silver Data Transformation

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import col, regexp_extract

# COMMAND ----------

df = spark.read.format('delta')\
    .option('header', True)\
    .option('inferSchema', True)\
    .load('abfss://bronze@netflixprojectdatabricks.dfs.core.windows.net/netflix_titles')

# COMMAND ----------

display(df)

# COMMAND ----------

df = df.fillna(
    {
        "duration_minutes": 0,
        "duration_seasons": 1
      }
      )

# COMMAND ----------

display(df)

# COMMAND ----------

df = df.filter(regexp_extract(col('duration_minutes'), '[a-zA-Z]', 0) == "")

# COMMAND ----------

display(df)

# COMMAND ----------

df = df.withColumn('duration_minutes', col('duration_minutes').cast(IntegerType()))\
    .withColumn('duration_seasons', col('duration_seasons').cast(IntegerType()))

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

display(df)

# COMMAND ----------

df = df.withColumn('short_title', split(col('title'), ':')[0])
display(df)

# COMMAND ----------

df = df.withColumn('rating', split(col('rating'), '-')[0])
display(df)

# COMMAND ----------

df = df.withColumn('type_flag', when(col('type')=='Movie', 1)\
    .when(col('type')=='TV Show', 2)\
    .otherwise(0))
display(df)


# COMMAND ----------

from pyspark.sql.window import Window

# COMMAND ----------

df = df.withColumn("duration_ranking", dense_rank().over(Window.orderBy(col("duration_minutes").desc())))
display(df)

# COMMAND ----------

# df.createOrReplaceTempView("temp_view_a")

# COMMAND ----------

# df.createOrReplaceGlobalTempView("temp_view_b")

# COMMAND ----------

# sql_a = spark.sql("""
#     SELECT * from temp_view_a
# """)


# sql_b = spark.sql("""
#                   Select * from global_temp.temp_view_b
#                   """)



# COMMAND ----------

df_visual = df.groupBy("type").agg(count("*").alias("count"))
display(df_visual)

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("path", "abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_titles")\
    .save()