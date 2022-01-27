SHELL := /opt/homebrew/bin/fish

run:
	FLASK_ENV=development FLASK_APP=mental_unload flask run

migration-init:
	flask db init

migration-gen:
	flask db migrate

migration-run:
	flask db upgrade

venv-create:
	virtualenv .venv

# venv-on:
# 	source .venv/bin/activate.fish

# venv-off:
# 	. deactivate