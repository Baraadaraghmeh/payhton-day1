from flask import Flask , render_template 
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "This is the index page"

@app.route('/hello')
def route_1():
    
    return "Hello world"

@app.route('/members')
def route_2():
    return 'Members Page'

if __name__=='__main__':
    app.run()
#q2...............................................
from flask import Flask , render_template 
app=Flask(__name__)  

@app.route('/<int:score>')
def hello_world(score):
    return render_template("index.html",marks=score)

if __name__=='__main__':
    app.run()
    
#q3.......................................................
from flask import Flask , render_template 
app=Flask(__name__)  

@app.route('/')
def hello_world(score):
    return render_template("index.html")

if __name__=='__main__':
    app.run()
    
    
    