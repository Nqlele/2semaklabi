from flask import Flask, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from os import path
from db.models import users
from flask_login import LoginManager
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6  # Импортируем Blueprint для lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from lab10 import lab10

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_users(user_id):
    return users.query.get(int(user_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '666')
app.config['DB_TYPE'] = os.environ.get('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'eremin_orm'
    db_user = 'eremin_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "eremin_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(lab10)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

@app.errorhandler(500)
def server_error(err):
    return "Ошибка сервера", 500

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab2">Вторая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab3">Третья лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab4">Четвертая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab5">Пятая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab6">Шестая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab7">Седьмая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab8">Восьмая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab9">Девятая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab9">Деcятая лабораторная</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Еремин Захар Дмитриевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)