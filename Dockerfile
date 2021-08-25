FROM python:3.9-slim-bullseye

COPY requirements/production.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY balancer/ /app/balancer/
WORKDIR /app

EXPOSE 80
CMD sanic balancer.server.app --host=0.0.0.0 --port=80 --workers=4
