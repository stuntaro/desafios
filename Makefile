.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: reddit_search
reddit_search:
	docker exec -i crawlers_api bash -c "python reddit.py ${subs} --score=${score}"

.PHONY: tests
tests:
	docker exec -i crawlers_api bash -c "pip install -r dev-requirements.txt"
	docker exec -i crawlers_api bash -c "coverage run -m pytest"
	docker exec -i crawlers_api bash -c "coverage report -m"