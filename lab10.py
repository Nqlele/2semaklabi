from flask import Blueprint, render_template, request, redirect, url_for, session, make_response, jsonify
from functools import wraps

lab10 = Blueprint('lab10', __name__)

# Пример данных для статей
articles = []

# Декоратор для проверки авторизации
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('lab10.login'))
        return f(*args, **kwargs)
    return decorated_function

@lab10.route('/lab10/')
def index():
    return render_template('lab10/index.html', articles=articles)

@lab10.route('/lab10/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Логика регистрации
        session['user_id'] = 1  # Пример ID пользователя
        return redirect(url_for('lab10.index'))
    return render_template('lab10/register.html')

@lab10.route('/lab10/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Логика авторизации
        session['user_id'] = 1  # Пример ID пользователя
        resp = make_response(redirect(url_for('lab10.index')))
        if 'remember_me' in request.form:
            resp.set_cookie('user_id', '1', max_age=30*24*60*60)
        return resp
    return render_template('lab10/login.html')

@lab10.route('/lab10/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('lab10.index'))

@lab10.route('/lab10/create_article', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        articles.append({'title': title, 'content': content})
        return redirect(url_for('lab10.index'))
    return render_template('lab10/create_article.html')

@lab10.route('/lab10/edit_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles[article_id]
    if request.method == 'POST':
        article['title'] = request.form['title']
        article['content'] = request.form['content']
        return redirect(url_for('lab10.index'))
    return render_template('lab10/edit_article.html', article=article, article_id=article_id)

@lab10.route('/lab10/delete_article/<int:article_id>')
@login_required
def delete_article(article_id):
    articles.pop(article_id)
    return redirect(url_for('lab10.index'))