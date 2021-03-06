from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User


# HOME
@app.route('/')
@app.route('/index')
def index():
    
    user = {'username': 'cat'}

    return render_template('index.html', user=user)


# LOGGING IN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember.data)
        return redirect(url_for('admin'))

    return render_template('login.html', title='Sign in', form=form)


# LOGGING OUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ADMIN PANEL
@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', title="Admin Panel")