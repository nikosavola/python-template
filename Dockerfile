FROM python:3.9.6-slim

LABEL version="0.1" \
    description="Python template" \
    org.opencontainers.image.source="https://github.com/nikosavola/python-template"

COPY . /src
WORKDIR /src

RUN pip install -e . --no-cache-dir

ENTRYPOINT ["python", "project_name/main.py"]