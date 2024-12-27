from flask import Blueprint, render_template, request, session, jsonify
# Создаём Blueprint для lab6
lab6_bp = Blueprint('lab6', __name__)

@lab6_bp.route('/lab6/')
def lab6_page():
    return render_template('lab6/lab6.html')
lab6_bp = Blueprint('lab6', __name__)

@lab6_bp.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    method = data.get('method')
    params = data.get('params')
    id = data.get('id')

    if method == 'info':
        return jsonify({
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        })
    elif method == 'booking':
        login = session.get('login')
        if not login:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': 1,
                    'message': 'Unauthorized'
                },
                'id': id
            })
        office_number = params
        for office in offices:
            if office['number'] == office_number:
                if office['tenant']:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    })
                office['tenant'] = login
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })
    elif method == 'cancellation':
        login = session.get('login')
        if not login:
            return jsonify({
                'jsonrpc': '2.0',
                'error': {
                    'code': 1,
                    'message': 'Unauthorized'
                },
                'id': id
            })
        office_number = params
        for office in offices:
            if office['number'] == office_number:
                if not office['tenant']:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Not booked'
                        },
                        'id': id
                    })
                if office['tenant'] != login:
                    return jsonify({
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 4,
                            'message': 'Not your booking'
                        },
                        'id': id
                    })
                office['tenant'] = ""
                return jsonify({
                    'jsonrpc': '2.0',
                    'result': 'success',
                    'id': id
                })
    return jsonify({
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    })