ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down

show-logs:
	sudo docker compose logs

migrate:
	docker compose exec web python3 manage.py migrate

makemigrations:
	docker compose exec web python3 manage.py makemigrations

superuser:
	sudo docker compose exec web python3 manage.py createsuperuser

collectstatic:
	docker compose exec web python3 manage.py collectstatic --no-input --clear

down-v:
	docker compose down -v

volume:
	docker volume inspect postgres_data

pytest:
	docker compose exec web pytest

test:
	docker compose exec web pytest -p no:warnings --cov=.

test-html:
	docker compose exec web pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker compose exec web flake8 .

