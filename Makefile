brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-games:
	poetry run brain-games

brain-gcd:
	poetry run brain-gcd

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression

build:
	poetry build

lint:
	poetry run flake8 brain_games

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

