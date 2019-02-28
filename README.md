*working on frontend and exceptions*

Book Review
============

Implemented a book review web applicaton following requirements provided by [WEB50](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/) using **Flask**, **Jinga2**, **SQLAlchemy** and a **PostgreSQL database** hosted on [ElephantSQL](https://www.elephantsql.com/).
 
What I learnt:
--------------
* Backend development and setting up routes to interact with frontend elements.
* Sessions and how they can be used to implement user accounts.
* Implementing raw SQL queries in an actual application using SQLAlchemy.
* Understanding HTTP methods GET and POST.
* Using requests to interact with the [GoodReads API](https://www.goodreads.com/api) and accessing JSON objects.

Usage
======

1. ```python -m pip install -r requirements.txt``` to install necessary packages.
2. Open cmd and cd to the repo and ```set FLASK_APP=application.py```(for windows) or ```export FLASK_APP=application.py``` for UNIX.
3. ```set DATABASE_URL=<database_url>``` where database_url is the PostgreSQL database.
4. ```python -m flask run``` to start the application.
