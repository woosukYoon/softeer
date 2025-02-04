from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from datetime import datetime
import time

spark = SparkSession.builder.appName("NYC_Taxi_Analysis_W5M2").config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()

def load_data(file_path) :
    taxi_df = spark.read.parquet(file_path)
    return taxi_df

def clean_data(taxi_df) :
    # 데이터셋의 관측 시점에 벗어난 데이터 제한
    cleaned_df = taxi_df.filter(f.col('tpep_pickup_datetime').isNotNull())\
        .filter(f.col('tpep_pickup_datetime').isNotNull())\
        .filter(f.col('trip_distance').isNotNull())\
        .filter(datetime(2022,1,1) <= f.col('tpep_pickup_datetime')) \
        .filter(f.col('tpep_pickup_datetime')<= datetime(2022,1,31))\
        .filter(f.col('tpep_pickup_datetime').isNotNull())
    return cleaned_df

def transform_data(cleaned_df) :

    # 1명 이상 승객을 대상으로 분석 진행
    df = cleaned_df.filter(f.col('passenger_count') > 1)

    # 날짜 형식 변환
    df = df.withColumn('pickup_date', f.to_date(f.col('tpep_pickup_datetime')))

    # Daily 집계 구하기
    transformed_df = df.groupBy('pickup_date').agg(
        f.count('*').alias("Daily_trip_count"),
        f.sum('total_amount').alias("Daily_revenue"),
        f.mean('trip_distance').alias("Daily_average_trip_distance")
    )

    # 날짜 순으로 정렬
    transformed_df = transformed_df.orderBy('pickup_date')

    return transformed_df

def action(transformed_df) :
    time.sleep(30)
    # 변환된 데이터프레임 출력
    transformed_df.show(5)
    time.sleep(30)

    # daily_df = transformed_df.collect()
    transformed_df.coalesce(1).write.csv(path = './ouput/dialy_results_plural.csv', mode = 'overwrite', header = True)

if __name__ == '__main__' :
    taxi_df = load_data('./NYC_TLC_Trip_Data/yellow_tripdata_2022-01.parquet')
    cleaned_df = clean_data(taxi_df)
    transformed_df = transform_data(cleaned_df)
    action(transformed_df)