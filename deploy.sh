#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@master:/home/jenkins/docker-compose.yaml
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file /home/jenkins/docker-compose.yaml myapp
