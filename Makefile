serve:
	#python manage.py runserver
	./manage.py runserver

migrate:
	./manage.py migrate

migrations:
	./manage.py makemigrations $(app)

collectstatic:
	./manage.py collectstatic

app:
	#django-admin startapp <name>
	./manage.py startapp $(name)
