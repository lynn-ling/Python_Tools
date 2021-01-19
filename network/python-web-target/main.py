# coding=UTF-8
from flask import  Flask, request, render_template,jsonify,redirect,Response,make_response,current_app
import sys, getopt
import logging
import time
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

opt_port = 5001
server_tag = "default"
logger = logging.getLogger("app.module")

@app.route('/csrf', methods=["GET", "POST"])
def csrf():
    return '<html><body>隐藏了csrf的页面<input type="hidden" name="csrf" value="csrfsecr"/></body></html>'




@app.route('/', methods=["GET", "POST", "PUT", "DELETE", "OPTION"])
def index():
    printDetail()
    data = {
        "param":printDetail(),
        "port":opt_port
    }
    return render_template("index.html",data = data) 


@app.route('/test', methods=["GET", "POST"])
def test():
    return printDetail()

@app.route('/desc', methods=["GET", "POST"])
def test1():
    return printDetail()

@app.route('/db', methods=["GET", "POST"])
def db():
    return printDetail()

@app.route('/testDocument', methods=["GET", "POST"])
def testDocument():

    resp = printDetail()
    return resp


@app.route('/jsonLogin', methods=["GET", "POST"])
def jsonLogin():

    data = {
        "code": "201",
    }
    res = make_response(data) # 设置响应体
    res.status = '200' # 设置状态码
    res.headers['token'] = "123456" # 设置响应头
    res.headers['City'] = "shenzhen" # 设置响应头

    return res

@app.route('/wait', methods=["GET", "POST"])
def wait():
    times = request.args.get("times")
    time.sleep( int(times) )
    return Response(), 200, {"wait": "5"}


@app.route('/json', methods=["GET", "POST"])
def jsonRes():
    return jsonObj()


@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    printDetail()
    if username=="user" and password == "pwd":
        return redirect("/")

    username = request.args.get("username")
    password = request.args.get("password")

    if username=="user" and password == "pwd":
        return redirect("/")

    response = Response()

    return response, 401, {"msg": "fidden"}

@app.route('/status', methods=["GET", "POST"])
def status():
    status = request.args.get("status")
    response = Response()
    response.data= "success"
    return response, status, {"msg": "fidden"}


@app.route('/phone', methods=["GET", "POST"])
def phone():

    current_app.logger.info(str(request.form.to_dict()))
    response = Response()
    response.data= 'OK'
    response.content_type="text/plain; charset=utf-8"
    return response, 200 



@app.route('/v2.0/fact/query', methods=["GET", "POST"])
def factquery():

    current_app.logger.info(str(request.form.to_dict()))
    response = Response()
    response.data= 'OK'
    response.content_type="text/plain; charset=utf-8"
    time.sleep( 20)
    return response, 200 

def jsonObj():
      
    data = {
        "code": -1,
        "msg": "hello world",
        "data": "hello world"
    }

    return jsonify(data)


def printDetail():

    headers= []
    for header in request.headers:
        headers.append(header[0]+":"+header[1])

    msg = {
        "server tag & port":str(server_tag + " & " + str(opt_port)),
        "host":request.host,
        "path":request.path,
        "header":headers,
        "args":request.args.to_dict(),
        "form":request.form.to_dict(),
        "json":request.json,
        "cookies":json.dumps(request.cookies,sort_keys = True, indent=4)
    }
    
    msgJSON = json.dumps(msg,sort_keys = True, indent=4)
    current_app.logger.info(msgJSON)
    return msgJSON

if __name__ == '__main__':
    argv = sys.argv[1:]
    opt_ip = '0.0.0.0'

    
    try:
        options, args = getopt.getopt(argv, "p:i:t:", ["help", "ip=", "port=", "tag="])

    except getopt.GetoptError:
        app.run(host=opt_ip,port=opt_port)
        sys.exit()
        
    for option, value in options:
        if option in ("-i", "--ip"):
            opt_ip = value
        if option in ("-p", "--port"):
            opt_port = value
        if option in ("-t", "--tag"):
            server_tag = value
    app.debug =True
    app.run(host=opt_ip,port=opt_port)
    


@app.errorhandler(Exception)
def error_handler(e):
  
    data = {
        "code": -1,
        "msg": str(e),
        "data": None
    }

    return jsonify(data)
