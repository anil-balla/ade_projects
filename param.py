# Databricks notebook source
# Example: Dynamic table processing based on parameters
# dbutils.widgets.text("schema_name", "sales")
# dbutils.widgets.text("table_name", "transactions")
# dbutils.widgets.text("process_date", "")



# COMMAND ----------

schema = dbutils.widgets.get("schema_name")
table = dbutils.widgets.get("table_name")
process_date = dbutils.widgets.get("process_date")

print(schema)
print(table)
print(process_date)



# COMMAND ----------


