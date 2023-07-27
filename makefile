install:
	poetry install

brain-games:
	poetry run brain-games

update:
	poetry update

build:
	poetry build

publish:
	poetry publish --dry-run

test: update build publish