from flask import Flask, render_template,request

'''
it creates an instance of the Flask class
which will be your WSGI(web server Gateway Interface ) application
'''
## WSGI Appication 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to the Flask course</H1></html>"

@app.route("/index1", methods=['GET'])
def index():
    return render_template('index1.html')  

@app.route("/about1")
def about():
    return render_template('about1.html')   

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
