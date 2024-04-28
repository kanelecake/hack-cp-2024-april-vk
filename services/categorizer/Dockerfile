FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install grpcio protobuf

COPY . /app
WORKDIR /app

RUN python -m pip install -r requirements.txt

ENV GRPC_PORT="18888"
EXPOSE $GRPC_PORT

ENTRYPOINT ["python", "main.py"]
