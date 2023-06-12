# Telegram filter service

This service received telegram messages from telegram groups, filter them and resend to another channel

### How to deploy

```shell
cd src
cp docker/prod.env.example docker/prod.env
vim docker/prod.env

docker-compose up --build -d
```

### How to run locally

```shell
cd src/bot
cp .env.example .env
vim .env

docker-compose up --build -d
```

### Session keys

About sessions please read [here](https://docs.telethon.dev/en/stable/concepts/sessions.html).

To generate session key use script `src/utils/generate_session_key.py`
