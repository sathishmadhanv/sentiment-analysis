from flask import url_for,redirect,render_template,request
import os
from PIL import Image
from app import utils
import glob

def base():
    return render_template('base.html') 
def index():
    return render_template('index.html')
def res():
    return render_template('result.html')

def Sentiment():
    if request.method=="POST":
        f=request.form['custom_tweet']
        r=utils.input(f)
        return render_template("senti.html",Upload=True,cus=r)
     

    return render_template("senti.html",Upload=False,cus=None,files=None)