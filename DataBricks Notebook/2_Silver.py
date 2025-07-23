# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Notebook Lookup Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ### Parameters

# COMMAND ----------

dbutils.widgets.text("source_folder", "netflix_directors")
dbutils.widgets.text("target_folder", "netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Variables

# COMMAND ----------

var_src_folder = dbutils.widgets.get("source_folder")
var_trg_folder = dbutils.widgets.get("target_folder")

# COMMAND ----------

df = spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load(f"abfss://bronze@netflixprojectdatabricks.dfs.core.windows.net/{var_src_folder}")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("path", f"abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/{var_trg_folder}")\
    .save()

# COMMAND ----------

