from flask import flask

app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def index():
    return 'Starting machine learning program'


if __name__=='main':
    app.run(debug = True)