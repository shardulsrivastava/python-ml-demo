#!/usr/bin/env bash

set -euo pipefail

# echo "Building App"
# docker build -f app/Dockerfile app/

echo "Building Backend"
docker build -f backend/Dockerfile backend/

echo "Running Backend"
docker run backend
