import argparse
from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(args):
    user = args.user
    password = args.password
    host = args.host
    db = args.db
    port = args.port
    table_name = args.table_name
    path = args.path
    
    # in order to download the file from the web, we can use the following command:
    # os.system()
    
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df_iter = pd.read_csv(path, iterator=True, chunksize=100000)
    
    df = next(df_iter)
    
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    df.head(n=0).to_sql(con=engine, name=table_name, if_exists="replace")

    for df in df_iter:
        start = time()

        # df = next(df_iter)

        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

        df.to_sql(name=table_name, con=engine, if_exists="append")

        end = time()

        print("inserted another chunk {:.3f} second".format(end - start))

    print("All chunks inserted into the database.")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
    description="Ingest data from csv file into postgres database",)

    parser.add_argument("--user", help="user name for postgres database", type=str)
    parser.add_argument("--password", help="password for postgres database", type=str)
    parser.add_argument("--host", help="host for postgres database")
    parser.add_argument("--db", help="database name for postgres database", type=str)
    parser.add_argument("--port", help="port number for postgres database", type=int)
    parser.add_argument("--table_name", help="table name for postgres database", type=str)
    parser.add_argument("--path", help="csv file to ingest", type=str)

    args = parser.parse_args()

    main(args)