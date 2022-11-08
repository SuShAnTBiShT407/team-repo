from flask import Flask, render_template, request, flash, Response
from werkzeug.utils import secure_filename
import wget
import cv2
import os
import calendar
import time
import getpass
import platform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VintageLab'


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


# Home Page of Vintage
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# About Page of Vintage
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    render_template('home.html')


@app.route('/effects', methods=['GET', 'POST'])
def effects():
    render_template('home.html')


# Main function-----
if __name__ == '__main__':
    app.run(debug=False, port=8080)
