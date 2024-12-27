from flask import Blueprint, render_template, request, abort, jsonify
lab7 = Blueprint('lab7', __name__)
@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')
films = [
    {
        "title": "Fast & Furious 6",
        "title_ru": "Форсаж 6",
        "year": 2013,
        "description": "После того как Доминик и Брайн побывали в Рио где они ограбили и свергли империю вора в законе, \
        их команда получила 100 миллионов, и наши герои оказались разбросаны по всему миру."
    },
    {
        "title": "Furious 7",
        "title_ru": "Форсаж 7",
        "year": 2015,
        "description": "Они покорили Токио и Рио, Лос-Анджелес и Лондон. \
        Но мир больше не играет по их правилам. Зной арабских пустынь, неприлично высокие небоскребы, миллионы долларов на колесах и очень, очень знаменитый злодей. \
        Скорость не знает границ."
    },
    {
        "title": "The Fate of the Furious",
        "title_ru": "Форсаж 8",
        "year": 2017,
        "description": "Гавана, Берлин, Нью-Йорк — для самой крутой команды в мире нет ничего невозможного, пока они вместе.\
        Но когда на их пути оказывается красотка и по совместительству королева киберпреступности Сайфер, дороги друзей расходятся."
    },
    {
        "title": "Furious 9",
        "title_ru": "Форсаж 9",
        "year": 2021,
        "description": "Доминик Торетто ведет спокойную жизнь в глуши вместе с Летти и сыном Брайаном, но опасность всегда где-то рядом.\
        Команде приходится снова собраться, чтобы спасти Мистера Никто после крушения самолёта, на котором перевозили пойманную хакершу Сайфер."
    },
    {
        "title": "Fast X",
        "title_ru": "Форсаж 10",
        "year": 2023,
        "description": "10 лет назад по заданию Агентства Доминик и Брайан ограбили бразильского политика,\
        бизнесмена и по совместительству наркобарона Эрнана Рейеса, который пустился за ними в погоню и погиб.\
        Теперь его сын Данте собирается реализовать коварный план мести — не просто убить Доминика, а заставить страдать, разделавшись с его семьёй."
    },
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        abort(404)
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        return jsonify(films[id])
        return '', 204
    else:
        abort(404)
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        if film['description'] == '':
            return {'description': 'Заполните описание'}, 400
        films[id] = film
        return jsonify(films[id])
    else:
        abort(404)
@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)
    if film['description'] == '':
            return {'description': 'Заполните описание'}, 400
    films.append(film)
    new_index = len(films) - 1
    return jsonify({"id": new_index}), 201