## Spark SQL Engine
- What is catalyst optimizer? 
- Spark SQL Engine.
- why we get analysis exception error ?
- what is physical planning / spark plan ?
- is spark engine a compiler ? Yes
- How many phases are invloved in spark SQL engine to convert a code into java byte code? 4
  
## RDD
 - What is RDD? 
   - Resilient distributed dataset.
 - when do we need an RDD?
 - Features of an RDD? 
 - what is dataframe / dataset?
 - why we should not use an RDD?
 - RDD is used for unstructured data and dataset, dataFrame api is used to structured data 

### Repartition and coalesce
- Use to manually partition the RDD. 
- Cannot partition the dataframe/dataset first need to convert it into the rdd and then repartition or coalesce happens.
- #### Difference between Repartition and RDD. 
  | Repartition                                  | Coalesce                              |
  | -------------------------------------------- | ------------------------------------- |
  | May decrease or incrase the no. of partition | Only decreases the no of partition.   |
  | a lot of data shuffling.                     | No data suffling at all.              |
  | Creates equal size of partitions.            | Creates uneven sized data partitions. |

### Joins in spark 
- types of joins in spark.
- join strategy in spark 
- #### shuffle sort merge join vs shuffle sort hash join 
  | Merge Join                                                | Hash Join                                                                  |
  | --------------------------------------------------------- | -------------------------------------------------------------------------- |
  | merge join is a CPU bound and does not require any memory | hash join takes in memory computation and can ran out of Out of RAM easily |
  | sparkby default uses merge join                           | sparkby default does not uses merge join                                   |
  | O(nlogn) Time complexity of a operation                   | O(1) Time complexity of a operation                                        |


