#!/usr/bin/env bash

set -euo pipefail

# echo "Building App"
# docker build -f app/Dockerfile app/

# mkdir ~/.ssh; touch ~/.ssh/id_rsa; chmod 400 ~/.ssh/id_rsa
# vi ~/.ssh/id_rsa # Add the key here

# cd /workspaces; git clone git@github.com:broadinstitute/ml4h.git
# cp ml4h/model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5 python-ml-demo/backend

#echo "Building Backend"
#docker build -f backend/Dockerfile backend/
#
#echo "Running Backend"
#docker run --rm -p 8081:8081 backend:v1

# echo "Testing the application"
#curl --header "Content-Type: application/json" \
#        --request POST \
#        --data '{"username":"xyz","password":"xyz"}' \
#        https://ubiquitous-sniffle-px76qgxr6rh6g6-8081.app.github.dev/test
#
#curl -v --header "Content-Type: application/json" \
#        --request POST \
#        --data '{"username":"xyz","password":"xyz"}' \
#        http://localhost:8081/test

# Check out Repository
# cd ../ && git lfs install --skip-smudge
# git clone https://github.com/shardulsrivastava/ml4h.git 
# cd ml4h/ 
# git config lfs.url https://github.com/shardulsrivastava/ml4h.git
# git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5

# Skip smudge - We'll download binary files later in a faster batch
# # git lfs install --force

echo "Building Images"
docker-compose build

echo "Running Application"
docker-compose up