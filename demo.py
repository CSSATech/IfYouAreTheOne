import logging
from flask import Flask, request
from handler import Handler


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
handler = Handler()

@app.route('/', methods=['GET', 'POST'])
def handle():
	if request.method == 'GET':
		return handler.get(request)
	elif request.method == 'POST':
		return handler.post(request)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
