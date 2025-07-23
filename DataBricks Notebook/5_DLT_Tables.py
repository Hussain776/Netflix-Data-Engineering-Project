# Databricks notebook source
# MAGIC
# MAGIC %md
# MAGIC # DLT Notebook - Gold Layer

# COMMAND ----------

# way to apply validation rules

look_tables_rule = {
    'rule1': "show_id is not null"
}

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_directors"
)

@dlt.expect_all_or_drop(look_tables_rule)

def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_directors")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_countries"
)

@dlt.expect_all_or_drop(look_tables_rule)

def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_category"
)

@dlt.expect_all_or_drop(look_tables_rule)

def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_category")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_cast"
)

@dlt.expect_all_or_drop(look_tables_rule)

def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_cast")
    return df

# COMMAND ----------

@dlt.table

def gold_stg_netflix_titles():
    
    df = spark.readStream.format("delta").load("abfss://silver@netflixprojectdatabricks.dfs.core.windows.net/delta/netflix_titles")
    return df

# COMMAND ----------

from pyspark.sql.functions import lit

# COMMAND ----------

@dlt.view

def gold_trns_netflix_titles_view():
    df = spark.readStream.table("LIVE.gold_stg_netflix_titles")
    df = df.withColumn("newFlag", lit(1))

    return df

# COMMAND ----------

master_data_rules = {
    "rule1": "newFlag is NOT NULL",
    "rule2": "show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table

@dlt.expect_all_or_drop(master_data_rules)

def gold_netflix_titles():
    df = spark.readStream.table("LIVE.gold_trns_netflix_titles_view")
    return df