from flask import Flask

app = Flask(__name__)

@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
	return last_name[0:3]+first_name[0:2]

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
