# chatapp

**Install postgresql**
***
	sudo apt-get update
	sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
	sudo su - postgres
	psql
***
	CREATE DATABASE chatapp;
	CREATE USER chatappuser WITH PASSWORD 'chatapp1234';
	ALTER ROLE chatappuser SET client_encoding TO 'utf8';
	ALTER ROLE chatappuser SET default_transaction_isolation TO 'read committed';
	ALTER ROLE chatappuser SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE chatapp TO chatappuser;

**Install virtuallenv**
***
	sudo apt-get install python3-pip
	sudo pip3 install virtualenv
	
	chatapp/ 
	virtualenv venv 
	source venv/bin/activate
	pip install -r requirements.txt
	
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver


***
	chatapp-frontend/ 
	npm install
	npm install buefy
	npm run dev
	
**Start - localhost:8080**