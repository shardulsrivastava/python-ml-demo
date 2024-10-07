#!/usr/bin/env bash

set -euo pipefail

# echo "Building App"
# docker build -f app/Dockerfile app/

echo "Building Backend"
docker build -f backend/Dockerfile backend/

echo "Running Backend"
docker run --rm -p 8081:8081 backend:v1

# echo "Testing the application"
curl --header "Content-Type: application/json" \
        --request POST \
        --data '{"username":"xyz","password":"xyz"}' \
        http://localhost:8081/predict

# Check out Repository
# cd ../ && git lfs install --skip-smudge
# git clone https://github.com/shardulsrivastava/ml4h.git 
# cd ml4h/ 
# git config lfs.url https://github.com/shardulsrivastava/ml4h.git
# git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5

# Skip smudge - We'll download binary files later in a faster batch
# # git lfs install --force