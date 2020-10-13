serve:
	#python manage.py runserver
	python3 manage.py runserver

migrate:
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations $(app)

collectstatic:
	python3 manage.py collectstatic

app:
	#django-admin startapp <name>
	python3 manage.py startapp $(name)
