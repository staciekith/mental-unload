req:
	pip3 install -r requirements.txt

run:
	FLASK_ENV=development FLASK_APP=mental_unload flask run

migration-init:
	FLASK_APP=mental_unload flask db init

migration-gen:
	FLASK_APP=mental_unload flask db migrate

migration-run:
	FLASK_APP=mental_unload flask db upgrade

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
# 	. deactivate