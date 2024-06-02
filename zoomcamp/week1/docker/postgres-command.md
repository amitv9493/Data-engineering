
### Create a docker network

    docker create network pg-network
    
### Build docker image

```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /home/amit/Desktop/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name=pg-database \
    postgres:13
```

### Connect with postgres server.

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

### Connect the pgadmin with the pgadmin

```bash 
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL='admin@admin.com' \
    -e PGADMIN_DEFAULT_PASSWORD='root' \
    -p 8080:80 \
    --name=pgadmin2 \
    --network=pg-network \
    dpage/pgadmin4

```
### Command to run the Python Script for data ingestion in postgres.
```bash
python3 ingest-data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --db=ny_taxi \
    --port=5432 \
    --table_name=yellow_taxi_data \
    --path=read.csv
```

docker run \
    --network=pg-network \
    taxi_data:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --db=ny_taxi \
    --port=5432 \
    --table_name=yellow_taxi_data \
    --path=read.csv




