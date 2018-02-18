from flask import Flask


app = Flask(__name__)

@app.route('/')
def handle():
	return 'hello_world'

if __name__ == '__main__':
	app.run()
