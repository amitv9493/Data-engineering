from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()
# Read a text file and count word frequencies

text_rdd = spark.sparkContext.textFile("/opt/spark/work-dir/data/input.txt")
counts = (
    text_rdd.flatMap(lambda line: line.split(" "))
    .map(lambda word: (word.lower(), 1))
    .reduceByKey(lambda a, b: a + b)
    .sortBy(lambda x: x[1], ascending=False)
)
# Save results

counts.saveAsTextFile("/opt/spark/work-dir/data/output")
spark.stop()
