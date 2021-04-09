#!/bin/bash
docker-compose pull && sudo -E DB_PASSWORD=
docker stack deploy --compose-file /home/jenkins/docker-compose.yaml myapp
