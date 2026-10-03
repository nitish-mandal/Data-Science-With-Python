from flask import Flask 
'''
it creates an instance of the Flask class
which will be your WSGI(web server Gateway Interface ) application
'''
## WSGI Appication 
app = Flask(__name__)

@app.route("/")
def welcome():
    return " Welcome to this  Flask course. this should be an amazing "

@app.route("/index")
def index():
    return " Welcome to this  Flask course.  this should be an amazing "    

if __name__ == "__main__":
    app.run(debug=True)

