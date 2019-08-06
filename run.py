from flask import Flask,render_template,jsonify,request
import requests
import random
app = Flask(__name__)

@app.route('/')
def hello_world():

    # r = requests.get('http://hq.sinajs.cn/list=M1909')
    # r = r.content.decode('gbk')
    # print(r)
    # return jsonify(r)
    return render_template('index.html')

@app.route('/updates')
def updates():
    d = {}
    # r = requests.get('http://hq.sinajs.cn/list=NI1910')
    # current = r.content.decode('gbk').split(',')[6].split('.')[0]
    # types = r.content.decode('gbk').split('str_')[1].split('=')[0]
    # d[types] = current

    d['test1'] = random.randint(1,10)
    d['test2'] = random.randint(100,200)
    d['test3'] = random.randint(1000,2000)
    
    
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True)
     