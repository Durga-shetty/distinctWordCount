from flask import Flask, request, render_template,redirect,url_for
import re
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def data():
    data = request.form['text_box']
    if request.method == 'POST':
      with open('text.txt', 'w') as f:
       f.write(str(data))
    return redirect(url_for('submit'))

@app.route('/submit')
def submit():
    list1=[]
    str1=""
    with open("text.txt","r") as f:
        for x in f:
            stripline=x.strip()
            list2=stripline.split()
            list1+=list2
    for ele in list1:
            str1+=ele
    x=re.findall("\W",str1)
    dict1={x:list1.count(x) for x in list1}
    return render_template('index.html',dict1=dict1,list1=list1,x=x)

@app.after_request
def before_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
        app.debug = True
        app.run()