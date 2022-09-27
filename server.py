from pickletools import read_bytes8
from flask import Flask,render_template,request,url_for,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template('index.html')


@app.route('/<string:page_name>')
def world1(page_name):
    return render_template(page_name)

def data(name):
    with open ('web/database.txt',mode='a') as a:
        email=name['email']
        subject=name['subject']
        message=name['message']
        return a.write(f'\n{email},{subject},{message}')
def data1(name):
    with open ('web/database.csv',newline='',mode='a') as a:
        email=name['email']
        subject=name['subject']
        message=name['message']
        file=csv.writer(a,delimiter=',',quotechar='"' , quoting=csv.QUOTE_NONE)
        return file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method  == 'POST':
        try:
            name=request.form.to_dict()
            print(name)
            data1(name)
            return redirect('/duplicate.html')
        except:
            return ' did not except this '
    else:
        return 'form not submitted'

                  