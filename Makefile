init: dc-up db-upgrade test-db-upgrade

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
	docker-compose -f docker-compose.dev.yml exec api flask db upgrade

# Create migration files if there are changes
db-migrate:
	docker-compose -f docker-compose.dev.yml exec api flask db migrate

freeze-req:
	docker-compose -f docker-compose.dev.yml exec pip3 freeze > requirements.txt

test:
	docker-compose -f docker-compose.dev.yml exec api python3 -m pytest tests/

test-path:
	docker-compose -f docker-compose.dev.yml exec api python3 -m pytest $(path)

test-db-upgrade:
	docker-compose -f docker-compose.dev.yml exec --env FLASK_ENV=test api flask db upgrade

coverage:
	docker-compose -f docker-compose.dev.yml exec api coverage run --omit="*/test*" -m pytest tests/
	docker-compose -f docker-compose.dev.yml exec api coverage report

# venv-create:
# 	virtualenv .venv

# venv-on:
# 	source .venv/bin/activate.fish

# venv-off:
# 	deactivate