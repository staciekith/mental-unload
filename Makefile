SHELL := /opt/homebrew/bin/fish

run-dev-app:
	FLASK_ENV=development FLASK_APP=mental_unload flask run

run-dev:
	FLASK_ENV=development FLASK_APP=$(app) flask run

venv-create:
	virtualenv .venv

# venv-on:
# 	source .venv/bin/activate.fish

# venv-off:
# 	. deactivate