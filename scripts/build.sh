#!/usr/bin/env bash

set -euo pipefail

# echo "Building App"
# docker build -f app/Dockerfile app/

echo "Building Backend"
docker build -f backend/Dockerfile backend/

echo "Running Backend"
docker run backend

# Check out Repository

# Skip smudge - We'll download binary files later in a faster batch
# git lfs install --skip-smudge

# Do git clone here
# git clone ...

# Fetch all the binary files in the new clone
# git lfs pull

# Reinstate smudge
# git lfs install --force
# git lfs pull --include model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5