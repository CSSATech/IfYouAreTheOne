from flask import Flask, request
from handler import Handle


app = Flask(__name__)
handler = Handle()

@app.route('/', methods=['GET', 'POST'])
def handle():
	if request.method == 'GET':
		return handler.get(request)
	elif request.method == 'POST':
		return handler.post(request)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
