from flask import Flask, render_template

'''
it creates an instance of the Flask class
which will be your WSGI(web server Gateway Interface ) application
'''
## WSGI Appication 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index1.html')  

@app.route("/about")
def about():
    return render_template('about1.html')      

if __name__ == "__main__":
    app.run(debug=True)