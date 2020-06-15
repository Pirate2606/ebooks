from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email
from models import Users

class Feedback(FlaskForm):

    email = StringField(validators = [InputRequired(), Email(message = 'Enter a valid email address.')])
    name = StringField(validators = [InputRequired()])
    message = TextAreaField(validators = [InputRequired()])
    submit = SubmitField('Alright, Submit')
# 
# class Request(FlaskForm):
#
#     name = StringField("Name : ", validators = [InputRequired()])
#     email = StringField("Email : ", validators = [InputRequired(), Email(message = 'Enter a valid email address.')])
#     semester = SelectField("Semester : ", validators = [InputRequired()], choices = [1,2,3,4,5,6,7,8])
#     branch = SelectField("Branch : ", validators = [InputRequired()], choices = ['CSE', 'IT', 'ECE', 'CE', 'EE'])
#     subject = SelectField(validators = [InputRequired()])
#     book = StringField("Name of book : ", validators = [InputRequired()])
#     submit = SubmitField('Alright, Submit')
