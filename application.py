import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use file system
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    # Setting login state (True if logged in) (False if logged out)
    if session.get("login_state") is None:
        session["login_state"] = False

    # Checking if logged in
    if session["login_state"]:
        return redirect(url_for('search'))
    else:
        return redirect(url_for('login'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None
    flag = True

    if request.method == 'POST':
        users = db.execute("SELECT * FROM users").fetchall()

        for user in users:
            if request.form['username'] == user.username:
                error = "This username already exists. Please choose another one!"
                flag = False
                break

        if flag:
            db.execute("INSERT INTO USERS (username, password) VALUES (:username, :password)",
                        { "username": request.form['username'], "password": request.form['password'] })
            db.commit()
            return redirect(url_for('login'))

    return render_template("signup.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        users = db.execute("SELECT * FROM users").fetchall()

        for user in users:
            if request.form['username'] == user.username and request.form['password'] == user.password:
                session['login_state'] = True
                return redirect(url_for('index'))

            else:
                error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session["login_state"] = False
    return redirect(url_for('index'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None

    db.commit()
    if request.method == 'POST':
        searchInput = request.form['search']

        search = db.execute("SELECT * FROM BOOKS WHERE bsn_id LIKE '%{}%' OR author LIKE '%{}%' OR title LIKE '%{}%'".format(searchInput, searchInput, searchInput))
        db.commit()
        return render_template("searchResults.html", search=search)

    return render_template("search.html")
