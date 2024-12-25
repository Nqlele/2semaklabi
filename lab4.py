from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)
@lab4.route('/lab4/')
def lab():
     return render_template('lab4/lab4.html')
@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')
@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/slozh-form')
def slozh_form():
    return render_template('lab4/slozh-form.html')
@lab4.route('/lab4/slozh', methods = ['POST'])
def slozh():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 0
    if x2 == '': x2 = 0
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/slozh.html', x1=x1, x2=x2, result=result)
@lab4.route('/lab4/umn-form')
def umn_form():
    return render_template('lab4/umn-form.html')
@lab4.route('/lab4/umn', methods = ['POST'])
def umn():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '': x1 = 1
    if x2 == '': x2 = 1
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/umn.html', x1=x1, x2=x2, result=result)
@lab4.route('/lab4/diff-form')
def diff_form():
    return render_template('lab4/diff-form.html')
@lab4.route('/lab4/diff', methods = ['POST'])
def diff():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/diff.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/diff.html', x1=x1, x2=x2, result=result)
@lab4.route('/lab4/step-form')
def step_form():
    return render_template('lab4/step-form.html')
@lab4.route('/lab4/step', methods = ['POST'])
def step():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/step.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 != 0 and x2 != 0:
        result = x1 ** x2
        return render_template('lab4/step.html', x1=x1, x2=x2, result=result)
    return render_template('lab4/step.html', error='Оба поля равны нулю!')

tree_count = 0
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')
    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1
    return render_template('lab4/tree.html', tree_count=tree_count)