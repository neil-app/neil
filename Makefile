web:
	npm --prefix presentation/web run dev

web_backend:
	pip install -r app/requirements.txt
	python app/manage.py runserver
