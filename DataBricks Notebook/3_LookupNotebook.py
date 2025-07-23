# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Array Parametrs

# COMMAND ----------


files = [
    {
        "source_folder": "netflix_cast",
        "target_folder": "netflix_cast"
    },
    {
        "source_folder": "netflix_category",
        "target_folder": "netflix_category"
    },
    {
        "source_folder": "netflix_countries",
        "target_folder": "netflix_countries"
    },
    {
        "source_folder": "netflix_directors",
        "target_folder": "netflix_directors"
    }
]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Job Utility to return Array

# COMMAND ----------

dbutils.jobs.taskValues.set(key="netflix_files_array", value=files)