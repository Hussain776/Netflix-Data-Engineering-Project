# Databricks notebook source
# MAGIC %md
# MAGIC # Incremental Data Loading Using AutoLoader

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog netflix_catalog;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create schema netflix_catalog.net_schema ;

# COMMAND ----------

checkpoint_Location = "abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/checkpoint"

raw_ext_loc = "abfss://raw@netflixprojectdatabricks.dfs.core.windows.net"

bronze_ext_loc = "abfss://bronze@netflixprojectdatabricks.dfs.core.windows.net"

# COMMAND ----------

df = spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_Location)\
  .load(raw_ext_loc)

# COMMAND ----------

display(df)

# COMMAND ----------

df.writeStream\
  .option("checkpointLocation", checkpoint_Location)\
  .trigger(availableNow=True)\
  .start("abfss://bronze@netflixprojectdatabricks.dfs.core.windows.net/netflix_titles")