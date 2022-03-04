init: dc-up db-upgrade

dc-up:
	docker-compose -f docker-compose.dev.yml up -d --build

dc-down:
	docker-compose -f docker-compose.dev.yml down

dc-exec-api:
	docker-compose -f docker-compose.dev.yml exec api $(cmd)

# Remove all stopped containers
d-prune:
	docker container prune

# Apply the existing migrations if not already done
db-upgrade:
	docker-compose -f docker-compose.dev.yml exec api flask db migrate

# Create migration files if there are changes
db-migrate:
	docker-compose -f docker-compose.dev.yml exec api flask db migrate

req:
	pip3 install -r requirements.txt

run:
	flask run

migration-init:
	flask db init

migration-gen:
	flask db migrate

migration-run:
	flask db upgrade

freeze-req:
	pip3 freeze > requirements.txt

test:
	python3 -m pytest tests/

test-path:
	python3 -m pytest $(path)

coverage:
	coverage run --omit="*/test*" -m pytest tests/ && coverage report

venv-create:
	virtualenv .venv

# venv-on:
# 	source .venv/bin/activate.fish

# venv-off:
# 	deactivate