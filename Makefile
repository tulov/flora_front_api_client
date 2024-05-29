all:
	@echo "make devenv		- Create & setup development virtual environment"
	@echo "make lint		- Check code with pylama"
	@echo "make clean		- Remove files created by distutils"
	@echo "make test		- Run tests"
	@echo "make sdist		- Make source distribution"
	@exit 0

clean:
	rm -fr *.egg-info dist

devenv: clean
	rm -rf venv
	# создаем новое окружение
	python3.8 -m venv venv
	# обновляем pip
	venv/bin/pip install -U pip
	# устанавливаем основные + dev зависимости из extras_require (см. setup.py)
	venv/bin/pip install -Ue '.[dev]'

lint:
	venv/bin/pylama

test: lint
	venv/bin/pytest -vv --cov=flora_front_api_client --cov-report=term-missing tests

sdist: clean
	# официальный способ дистрибуции python-модулей
	python3 setup.py sdist
