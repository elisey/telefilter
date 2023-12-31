FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8

ARG UID="1000"
ARG GID="1000"
ARG USER="user"

WORKDIR /project/

ADD pyproject.toml /project
ADD poetry.lock /project

RUN addgroup --gid $GID $USER && \
    adduser --uid $UID --gid $GID --disabled-password --gecos '' $USER && \
    usermod -aG sudo $USER && \
    echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    pip install --upgrade pip && \
    pip install poetry==1.4.1 certifi && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    mkdir /data

COPY service /project/service
ADD docker/prod.env /project/service/.env

COPY docker/entrypoint.sh /project/service/entrypoint.sh
RUN chmod +x /project/service/entrypoint.sh

WORKDIR /project/service

ENTRYPOINT ["/project/service/entrypoint.sh"]
