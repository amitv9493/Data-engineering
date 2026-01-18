import asyncio
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse


async def process_chunk(df, engine, table_name):
    print("inserting another chunk")
    start = time()
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    await df.to_sql(name=table_name, con=engine, if_exists="append")
    end = time()
    print("Inserted another chunk {:.3f} seconds".format(end - start))


async def main(args):
    user = args.user
    password = args.password
    host = args.host
    db = args.db
    port = args.port
    table_name = args.table_name

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df_iter = pd.read_csv("taxi_data.csv", iterator=True, chunksize=100000)
    df = next(df_iter)

    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    df.head(n=0).to_sql(con=engine, name=table_name, if_exists="replace")
    print("Table created.")

    tasks = []
    for df_chunk in df_iter:
        task = process_chunk(df_chunk, engine, table_name)
        tasks.append(task)
        print("addming one more task")

    await asyncio.gather(*tasks)

    print("All chunks inserted into the database.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ingest data from a CSV file into a PostgreSQL database"
    )

    parser.add_argument(
        "--user", help="user name for the PostgreSQL database", type=str
    )
    parser.add_argument(
        "--password", help="password for the PostgreSQL database", type=str
    )
    parser.add_argument("--host", help="host for the PostgreSQL database", type=str)
    parser.add_argument(
        "--db", help="database name for the PostgreSQL database", type=str
    )
    parser.add_argument(
        "--port", help="port number for the PostgreSQL database", type=int
    )
    parser.add_argument(
        "--table_name", help="table name for the PostgreSQL database", type=str
    )
    parser.add_argument("--path", help="CSV file to ingest", type=str)

    args = parser.parse_args()

    asyncio.run(main(args))
