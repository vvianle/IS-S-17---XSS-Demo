# Independence Study S'17 - XSS in Django Framework
##### Vivian Le '19 - Mount Holyoke College
##### Faculty Advisor: Professor Peter Klemperer
The project recreates XSS vulnerabilities in Django framework and investigates how its protection system works.

---
Demo installing guide:

If you have Python > 2.7 on your computer, pip is already installed for you. Otherwise, install pip:
	
	sudo easy_install pip

Install virtual environment:

	pip install virtualenv

Create a folder and clone the project from Git. cd into project folder and activate the virtualenv:
	
	source venv/bin/activate

To install the packages needed to run the project:
	
	pip install -r requirements.txt

To run Cookie project, cd cookie:

	python manage.py runserver 2000

To run BlogDemo project, cd tutorial7\ -\ srvup\ blog/src:

	python manage.py runserver 4000

To make a request from the command line, create a file or edit post.txt then:

	cat post.txt | nc localhost 2000

To exist virtualenv:

	deactivate
