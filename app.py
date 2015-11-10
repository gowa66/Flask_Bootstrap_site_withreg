from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps 
# import sqlite3


app = Flask(__name__)

app.secret_key = 'secret_key'
# app.datebase = "sample.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(app)

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap


@app.route('/')
@login_required
def home():
	# g.db = connect_db()
	# cur = g.db.execute('select * from posts')
	# posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	# g.db.close() 
	return render_template("home.html")



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

# def connect_db():
# 	return sqlite3.connect(app.datebase)

if __name__ == '__main__':
	app.run(debug=True)


