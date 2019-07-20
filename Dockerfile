ARG VERSION=3.6
FROM python:$VERSION

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /apps
ENV CONFIG_ROOT /config

RUN mkdir ${CONFIG_ROOT}
COPY apps/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

# Install PostgresSQL from binary
RUN pip install psycopg2-binary

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD apps/ ${APP_ROOT}

RUN python manage.py collectstatic --no-input
