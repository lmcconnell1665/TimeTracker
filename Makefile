setup:
	python3 -m venv ~/.TimeTracker

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv main_test.py
	#python -m pytest --nbval notebook.ipynb

lint:
	#hadolint Dockerfile 
	#main python files
	pylint --disable=C0301,W0612,C0303,W0611,C0411 main.py
	pylint main_test.py

	#django python files
	pylint --disable=C0415 DjangoWebApp/manage.py


all: install lint test
