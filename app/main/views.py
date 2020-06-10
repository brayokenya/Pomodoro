from flask import render_template
from . import main
from flask_login import login_required
@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/auth/login', methods=['GET', 'POST'])

# def login():
#     '''
#     view pitch function that returns pitch categories
#     '''
#     general = Pitch.query.all()
#         # return redirect(url_for('main.index'))

#     return render_template('auth/login.html')

# @main.route('/auth/register', methods=['GET', 'POST'])

# def login():
#     '''
#     view pitch function that returns pitch categories
#     '''
#     general = Pitch.query.all()
#         # return redirect(url_for('main.index'))

#     return render_template('auth/register.html')        