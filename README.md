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
------
1. ```python -m pip install requirements.txt``` to install necessary packages.
2. ```cd``` into directory and ```set FLASK_APP=application.py``` and ```set DATABASE_URL=<database_url>``` to set environment variables. (replace ```set``` with ```export``` if on UNIX).
3. Insert GoodReads API key in application.py
4. ```python -m flask run``` to start the application.
5. Open browser and type in ```localhost:5000``` or ```ctrl + right-click``` on 127.0.0.1:5000 in cli.
