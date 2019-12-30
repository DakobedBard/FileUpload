sudo docker kill djangoapp
sudo docker cp scripts/scrub.sql djangoupload_db_1:/scrub.sql && sudo docker exec djangoupload_db_1 psql -d db2 -U database1_role -f scrub.sql