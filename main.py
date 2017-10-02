from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    name = request.form['user-name']
    password = request.form['password']
    verify = request.form['verify-password']
    email = request.form['email']
    amt_name = len(name)
    amt_pass = len(password)
    amt_email = len(email)
    name_error = ""
    pass_error = ""
    ver_error= ""
    email_error = ""

    if amt_name <3 or amt_name >20 or amt_name == 0:
        name_error="Not a valid username"
    else:
        name = name
    
    for n in name:
        if n == ' ':
            name_error="User name cannot contain spaces"
        else:
            name = name
            
    if amt_pass <3 or amt_pass >20 or amt_pass == 0:
        pass_error="Not a valid password"
    for p in password:
        if p == ' ':
            pass_error="Password cannot contain spaces"

    if verify != password:
        ver_error="Password does not match"

    if amt_email != 0:
        if email.count("@") != 1 or email.count(".") != 1:
            email_error="Please enter a valid email"
    
        if amt_email <3 or amt_email >20:
            email_error="Please enter a valid email"
    else:
        email = email

    if not name_error and not pass_error and not ver_error and not email_error:
        return render_template('greeting.html', name=name)
    else:
        return render_template('welcome.html', name_error=name_error, pass_error=pass_error, 
            ver_error=ver_error, email_error=email_error, name=name, email=email)

app.run()