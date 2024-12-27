from flask import Flask, render_template, redirect, url_for, request, session, make_response
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Пример данных для статей
articles = []

# Декоратор для проверки авторизации
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html', articles=articles)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Логика регистрации
        session['user_id'] = 1  # Пример ID пользователя
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Логика авторизации
        session['user_id'] = 1  # Пример ID пользователя
        resp = make_response(redirect(url_for('index')))
        if 'remember_me' in request.form:
            resp.set_cookie('user_id', '1', max_age=30*24*60*60)
        return resp
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/create_article', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        articles.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('create_article.html')

@app.route('/edit_article/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = articles[article_id]
    if request.method == 'POST':
        article['title'] = request.form['title']
        article['content'] = request.form['content']
        return redirect(url_for('index'))
    return render_template('edit_article.html', article=article, article_id=article_id)

@app.route('/delete_article/<int:article_id>')
@login_required
def delete_article(article_id):
    articles.pop(article_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)