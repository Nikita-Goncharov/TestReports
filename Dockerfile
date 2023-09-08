FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /TestReports

COPY . /TestReports

RUN pip install -r requirements.txt

RUN chmod +x /TestReports/docker-entrypoint.sh
ENTRYPOINT ["sh", "/TestReports/docker-entrypoint.sh"]
