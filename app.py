# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps 
# import sqlite3

# create the aplication object
app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])


# create the sqlalchemy object
db = SQLAlchemy(app)



# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('login'))
	return wrap


@app.route('/')
@login_required
def home():
	posts = []
	try:

		g.db = connect_db()
		cur = g.db.execute('select * from posts')

		for row in cur.fetchall():
			posts.append(dict(title=row[0], description=row[1]))
	
		g.db.close()
	except sqlite3.OperationalError:
		flash("You have no database!") 
	return render_template("home.html", posts=posts)



@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Try again.'
		else:
			session['logged_in'] = True
			flash('You were successfully logged in')
			return redirect(url_for('home'))
	return render_template('login.html', error=error) 

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were successfully logged out')
	return redirect(url_for('home'))



if __name__ == '__main__':
	app.run()


