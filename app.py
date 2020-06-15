from models import app, db, Users, Blacklist
from flask import render_template, url_for, redirect, request
from flask_migrate import Migrate
from form import Feedback
import requests

Migrate(app, db)


def check_mail(email):
    url = "http://apilayer.net/api/check?access_key=91c73e5c9c8a1141a2f1a07ff7136df2&email=" + email + "&smtp=1&format=1"
    response = requests.get(url)
    response = response.content.decode("utf-8")
    response = response.replace("\n", "")
    response = response.replace("true", "True")
    response = response.replace("false", "False")
    response = response.replace("null", "None")

    dict = eval(response)

    if dict['format_valid'] == True and dict['smtp_check'] == True:
        return True
    else:
        return False


@app.route('/', methods = ['GET', 'POST'])
def home():

    form = Feedback()

    if form.validate_on_submit():

        mail = form.email.data
        name = form.name.data
        message = form.message.data

        try:
            ip = request.environ['HTTP_X_FORWARDED_FOR']
        except KeyError:
            ip = request.environ['REMOTE_ADDR']

        valid = check_mail(mail)

        if valid == True:
            user = Users(mail, name, message, ip)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return render_template('invalid.html')


    return render_template('home.html', form = form)

@app.route('/cse')
def first():
    return render_template('cse.html')


@app.route('/it')
def second():
    return render_template('it.html')


@app.route('/ce')
def third():
    return render_template('ce.html')


@app.route('/ee')
def fourth():
    return render_template('ee.html')


@app.route('/ece')
def fifth():
    return render_template('ece.html')


if __name__ == "__main__":
    app.run(debug = True)
