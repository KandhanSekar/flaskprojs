from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts,form=form)

@app.route('/login')
def login():

    return render_template('login.html', title='Sign In', form=form)