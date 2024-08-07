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

## Repartition and coalesce
- Use to manually partition the RDD. 
- Cannot partition the dataframe/dataset first need to convert it into the rdd and then repartition or coalesce happens.
- #### Difference between Repartition and RDD. 
  | Repartition                                  | Coalesce                              |
  | -------------------------------------------- | ------------------------------------- |
  | May decrease or incrase the no. of partition | Only decreases the no of partition.   |
  | a lot of data shuffling.                     | No data suffling at all.              |
  | Creates equal size of partitions.            | Creates uneven sized data partitions. |

## Joins in spark 
- types of joins in spark.
- join strategy in spark 
- #### shuffle sort merge join vs shuffle sort hash join 
  | Merge Join                                                | Hash Join                                                                  |
  | --------------------------------------------------------- | -------------------------------------------------------------------------- |
  | merge join is a CPU bound and does not require any memory | hash join takes in memory computation and can ran out of Out of RAM easily |
  | sparkby default uses merge join                           | sparkby default does not uses merge join                                   |
  | O(nlogn) Time complexity of a operation                   | O(1) Time complexity of a operation                                        |
- #### Broadcast Hash Join
  - Difference between broadcast hash and suffle hash join.
  - When it is bad?
    - If the smaller dataset is too large to fit in memory, broadcast hash join can lead to excessive memory consumption. Broadcasting data also requires additional memory on the driver node to hold the data before sending it to worker nodes.
  - When both tables are large, getting the broadcast join may lead to out-of-memory issues. In that case, Shuffle Hash Join can be a better option. 

## (Spark Memory Management) Driver out of Memory.
 - What is OOM?
 - Common reson for OOM?
    1. collect method is used.
    2. broadcast 
    3. more objects are used in the process.
    4. Wrong configuration.
   
 - ### Driver Memory 
  - only JVM process runs in `Spark.driver.memory`. (*if size is 1 GB* )
  - Non JVM Processes, container's processes and objects are saved in `spark.driver.memoryOverhead`. *(10% or 384 MB whichever is higher.)*

## Executer Memory Management (Executer OOM)
- [Watch this video for explainations](https://www.youtube.com/watch?v=b2hO1oJf9nA&list=PLTsNSGeIpGnGkpfKMf7ilFmzfx6AjMKyT&index=18)

## Spark Submit
```mermaid
graph LR;
    A[Start] --> B[Process];
    B --> C{Decision};
    C -->|Yes| D[End];
    C -->|No| B;
```