import json
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
from flask import render_template,request,abort,redirect,flash,make_response,session,url_for

#local import will follow
from pkg import app,csrf
#removed post and put registration
from pkg.models import db,User,ContactUs
from pkg.forms import *

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("user/index.html")
    else:
        fname = request.form.get("fname")
        mail = request.form.get("mail")
        msg = request.form.get("msg")
        cont = ContactUs(fullname=fname,email=mail,message=msg)
        db.session.add(cont)
        db.session.commit()
        flash("We'll reach out to you as soon as possible, thank you.")
    return render_template("user/index.html")

@app.route("/donate")
def donation():

    return render_template("user/payment.html")

@app.route("/volunteer", methods=["GET","POST"])
def volunteer():
    if request.method=="GET":
        return render_template("user/volunteer.html")
    else:
        digits = request.form.get("digits")
        fname = request.form.get("fname")
        msg = request.form.get("msg")
        user = User(fullname=fname,phone=digits,message=msg)
        db.session.add(user)
        db.session.commit()
        flash("Thank you for your efforts, You'll be contacted soon.")
        return render_template("user/volunteer.html")
        

    pass