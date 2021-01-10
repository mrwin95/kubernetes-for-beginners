from flask import Flask, render_template, request, make_response, g
import socket, os, json, random
app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/', methods=['GET'])
def index():
  res = make_response(render_template('index.html', hostname))
  return res

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80, debug=True, threaded=True)