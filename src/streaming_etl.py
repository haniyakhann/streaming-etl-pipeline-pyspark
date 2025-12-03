from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType


def main():
    # 1. Start Spark session
    spark = (
        SparkSession.builder
        .appName("StreamingETLPipeline")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    # 2. Define schema of incoming JSON events
    event_schema = StructType([
        StructField("event_id", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("event_ts", TimestampType(), True),
    ])

    # 3. Paths (relative to this src/ folder)
    input_path = "data/raw"
    checkpoint_path = "data/checkpoint"
    output_path = "output/curated"


    # 4. Read streaming JSON from input_path
    events_df = (
        spark.readStream
        .schema(event_schema)
        .json(input_path)
    )

    # 5. Basic cleaning / transformation
    cleaned_df = (
        events_df
        .filter(col("event_type").isNotNull())
        .withColumn("ingest_ts", current_timestamp())
    )

    # 6. Write to Parquet in append mode
    query = (
        cleaned_df.writeStream
        .format("parquet")
        .option("path", output_path)
        .option("checkpointLocation", checkpoint_path)
        .outputMode("append")
        .start()
    )

    print(f"Streaming ETL started. Watching folder: {input_path}")
    print(f"Writing output to: {output_path}")
    query.awaitTermination()


if __name__ == "__main__":
    main()
