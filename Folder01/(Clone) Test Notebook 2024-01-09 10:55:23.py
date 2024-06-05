# Databricks notebook source
print('hello')

# COMMAND ----------

# MAGIC %r

# COMMAND ----------

# MAGIC %scala

# COMMAND ----------

dbutils.fs.ls("/")

# COMMAND ----------

files = dbutils.fs.ls("file:/Workspace/Users")
display(files)

# COMMAND ----------

# MAGIC %fs ls file:/Workspace/Users/will.chow@databricks.com/

# COMMAND ----------

files = dbutils.fs.ls("/Workspace/Users/will.chow@databricks.com/")
display(files)
