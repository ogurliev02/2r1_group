from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Welcome Home!'

@app.route('/user')
def user():
    user = {'username': 'Mark'}
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }, 
        {
            'author': {'username': 'Gamid'},
            'body': 'Super text!'
        }
    ]

    return render_template('user.html', user=user, title='User', posts=posts)