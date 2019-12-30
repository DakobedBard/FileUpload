#! /bin/bash

sudo docker exec -it djangoupload_db_1 psql -d database1 -U database1_role
