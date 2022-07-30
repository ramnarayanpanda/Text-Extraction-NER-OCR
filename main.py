from flask import Flask, request  
from flask import render_template 


app = Flask(__name__)  
app.secret_key = 'document_scanner_app'


@app.route('/') 
def index(): 
    # return "hello world1"
    return render_template('index.html')

if __name__ == '__main__':
    # debug=True means if you make any changes to the code 
    # automatically the program will get refreshed
    app.run(debug=True)   
    
    