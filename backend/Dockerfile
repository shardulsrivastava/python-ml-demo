FROM ghcr.io/broadinstitute/ml4h:4fd4656-cpu
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8081
CMD ["fastapi", "run", "main.py", "--port", "8081"]