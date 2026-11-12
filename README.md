# Starting a spark cluster

```bash
docker compose up -d
```

# Submitting a pyspark job.

## example pyspark job. wordcount.py - simple PySpark word count job

```python
from py_spark.sql import SparkSession

spark = SparkSession.builder
.appName("WordCount")
.getOrCreate()

# Read a text file and count word frequencies

text_rdd = spark.sparkContext.textFile("/opt/spark/work-dir/data/input.txt")
counts = text_rdd.flatMap(lambda line: line.split(" "))
.map(lambda word: (word.lower(), 1))
.reduceByKey(lambda a, b: a + b)
.sortBy(lambda x: x[1], ascending=False)

# Save results

counts.saveAsTextFile("/opt/spark/work-dir/data/output")
spark.stop()

```

## Copy the script into the master container.

```bash
docker cp wordcount.py spark-master:/opt/spark/work-dir/
```

## Submit it

```bash
docker exec spark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /opt/spark/work-dir/wordcount.py
```