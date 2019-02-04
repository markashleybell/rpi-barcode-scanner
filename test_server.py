import subprocess
from bottle import run, post, request, response, get, route


@route('/', method = 'GET')
def index():
    return "OK"

@route('/registercode', method = 'POST')
def registercode():
    code = request.forms.get('code')
    with open('codes', 'a') as f:
        f.write(code + '\n')
    return "OK"

run(host='192.168.78.12', port=8080, debug=True)
