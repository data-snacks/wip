https://github.com/mvillarrealb/docker-spark-cluster/tree/master
https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4
https://medium.com/@SaphE/testing-apache-spark-locally-docker-compose-and-kubernetes-deployment-94d35a54f222

# How to obtain the id

docker ps --format '{{.Names}} {{.ID}}' - Or in the master localhost

# Using the container Id to get into the Spark Console

docker exec -i -t [YOUR CONTAINER ID] /bin/bash

# Run the spark command.

/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
--driver-memory 1G \
--executor-memory 1G \
/opt/spark-apps/main.py