

FORCE:

dev:
	python -m pip install --upgrade pip
	pip install -r requirements.txt --upgrade

tests:
	pytest

prod: tests
	git commit -a
	git push origin main
