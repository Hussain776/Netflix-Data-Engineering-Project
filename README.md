# Netflix Data Engineering Project 🎥🚀

An end-to-end modern data engineering project that leverages the Azure ecosystem and Databricks to build an automated, scalable ETL pipeline using Medallion Architecture.

> 👏 Inspired by [Ansh Lamba](https://www.youtube.com/@anshlamba) — this project replicates and expands on his Netflix ETL pipeline walkthrough.

---

## ✨ Overview

This project demonstrates how to:

* Extract data from GitHub
* Load it into **Azure Data Lake Gen2**
* Transform it using **Databricks Notebooks** and **Delta Live Tables**
* Implement a **medallion architecture** with `raw`, `bronze`, `silver`, and `gold` layers
* Use **Azure Data Factory** for orchestration
* Manage secrets securely using **Azure Key Vault**
* Apply Unity Catalog for data governance and RBAC

---

## 🔧 Services Used

* **Azure Data Factory (ADF)**
* **Azure Data Lake Storage Gen2**
* **Azure Key Vault**
* **Azure Databricks** (with Delta Lake, Delta Live Tables)
* **Unity Catalog**
* **GitHub** (data source)

---

## 📆 Daily Progress Logs

### 📅 Day 1: Project Setup and Planning

* Defined objectives, tools, architecture
* Created resource group and Azure services

### 📅 Day 2: Data Ingestion Setup

* Created containers in ADLS Gen2: `raw`, `bronze`, `silver`, `gold`
* Used ADF to fetch Netflix dataset from GitHub into the `raw` layer

### 📅 Day 3: Secure Connectivity

* Used Azure Key Vault to store secrets (GitHub URL, tokens, storage keys)
* Linked Key Vault with ADF and Databricks

### 📅 Day 4: Databricks + Unity Catalog

* Created workspace and metastore
* Configured Unity Catalog with ADLS
* Registered external locations and volumes

### 📅 Day 5: Bronze Layer Transformation

* Created DLT pipelines to clean and ingest raw data into `bronze`
* Implemented schema inference and column renaming

### 📅 Day 6: Silver Layer Transformation

* Removed nulls, deduplicated records, casted data types
* Partitioned & optimized with ZORDER

### 📅 Day 7: Gold Layer Insights

* Aggregated KPIs like count by country, genre, and release year
* Created final tables for reporting and dashboards

---

## 🚀 Architecture Diagram

![Architecture Flow](./images/architecture-diagram.png)

## 🚀 Delta Live Tables Flow

![DLT Flow](./images/delta-live-tables.png)

---

## ✨ Key Learnings

* Orchestrating data pipelines in ADF
* Using Unity Catalog for secure lakehouse governance
* Writing production-grade notebooks using DLT
* Implementing the Medallion Architecture in practice

---

## 🌟 Let’s Connect!

If you're working on similar projects or looking to collaborate, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/yourprofile).

---
