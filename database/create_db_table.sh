#!/bin/bash

DB_NAME="radix_challenge"
DB_USER="postgres"
DB_PASS="admin"
DB_HOST="localhost"
DB_PORT="5432"
TABLE_NAME="data_sensor"

export PGPASSWORD=$DB_PASS

psql_cmd() {
  psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $1 -tc "$2"
}

psql_exec() {
  psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $1 -c "$2"
}

create_db_if_not_exists() {
  psql_cmd "$DB_USER" "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME';" | grep -q 1

  if [ $? -ne 0 ]; then
    createdb -U $DB_USER -h $DB_HOST -p $DB_PORT $DB_NAME
  else
    echo "Database '$DB_NAME' already exists."
  fi
}

create_table_if_not_exists() {
  psql_cmd "$DB_NAME" "SELECT 1 FROM information_schema.tables WHERE table_name = '$TABLE_NAME';" | grep -q 1

  if [ $? -ne 0 ]; then
    psql_exec "$DB_NAME" "
    CREATE TABLE $TABLE_NAME (
      id SERIAL PRIMARY KEY,
      equipamentId VARCHAR(100) NOT NULL,
      value NUMERIC NOT NULL,
      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"
  else
    echo "Table '$TABLE_NAME' already exists"
  fi
}

create_db_if_not_exists
create_table_if_not_exists