#######################################################
#           >File Name: flask_client.py
#           > Author: Wuzongjing
#           >Mail:wuzongjing@163.com
#           >Created Time: Sat 12 Dec 2020 15:55 PM CST
#######################################################

from flask import Flask,send_file
import sys

app=Flask(__name__)

@app.route('/index')
def index():
    return send_file('templates/index.html')

@app.route('/album')
def album():
    return send_file('templates/album.html')

@app.route('/about')
def about():
    return send_file('templates/about.html')

# @app.route('/contact')
# def contact():
#     return send_file('templates/contact.html')

@app.route('/blog')
def blog(username):
    return send_file('templates/blog.html')

@app.route('/register')
def register():
    return send_file('templates/register.html')
@app.route('/login')
def login():
    return send_file('templates/login.html')
@app.route('/info')
def info(username):
    return send_file('templates/info.html')



if __name__ == '__main__':
    app.run(debug=True)