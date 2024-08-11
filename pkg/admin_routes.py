import random,os,string
from flask import render_template,request,abort,redirect,flash,make_response,session,url_for

#local import will follow
from pkg import app,csrf
#removed post and put registration
from pkg.models import db,Admin,ContactUs,User
from pkg.forms import *

@app.route("/admin/login/", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        # Retrieve data from form
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        
        # Check if username exists in the database
        admin_user = "thecheat23"
        if admin_user:
            # Verify password
            if admin_pwd == pwd:
                # Passwords match, save user ID in session
                session["adminuser"] = admin_user
                session['role'] = 'admin'
                
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid password or Invalid username', category='error')
        else:
            flash('Invalid password or Invalid username', category='error')
        
        return redirect(url_for('admin_login'))

@app.route("/admin_dashboard")
def admin_dashboard():
    if session.get('adminuser')==None or session.get('role')!= 'admin':
         return redirect(url_for('admin_login'))
    else:
        books =db.session.query(ContactUs).all()
        return render_template("admin/index.html",books=books)
    return render_template("admin/index.html")

@app.route("/view")
def view_volunteers():
    if session.get('adminuser')==None or session.get('role')!= 'admin':
         return redirect(url_for('admin_login'))
    else:
        books =db.session.query(User).all()
        return render_template("admin/view.html",books=books)
    return render_template("admin/index.html")

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        # Retrieve form data
        current_password = request.form['currentPassword']
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']
        
        # Retrieve admin user from database (assuming username is unique)
        admin_user = Admin.query.filter_by(admin_username='lady@admin').first()
        
        # Check if current password matches the password in the database
        if admin_user.admin_pwd != current_password:
            flash('Incorrect current password.', 'error')
            return redirect(url_for('change_password'))

        # Check if new password matches the confirm password
        if new_password != confirm_password:
            flash('New password and confirm password do not match.', 'error')
            return redirect(url_for('change_password'))

        # Update the admin user's password in the database
        admin_user.admin_pwd = new_password
        db.session.commit()

        flash('Password changed successfully!', 'success')
        return redirect(url_for('change_password'))
    
    return render_template('admin/change_pwd.html')

@app.after_request
def after_request(response):
    # To Solve The problem of logged out users details being cache in the brower
    response.headers["Cache-control"]="no-cache, no-store, must-revalidate"
    return response

@app.route("/admin/logout/")
def admin_logout():
    if session.get("adminuser")!=None:#he is still logged in
        session.pop("adminuser",None)
        session.pop("role",None)
        flash("You have Logged out", category='info')
        return redirect(url_for('admin_login'))
    else:#she is logged out already
        return render_template(url_for('admin_login'))
