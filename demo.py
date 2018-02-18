from flask import Flask, request
from handler import Handle


app = Flask(__name__)
handler = Handle()

@app.route('/', methods=['GET', 'POST'])
def handle():
	if request.method == 'GET':
		handler.get(request)
	elif request.method == 'POST':
		handler.post(request)

if __name__ == '__main__':
	app.run()
