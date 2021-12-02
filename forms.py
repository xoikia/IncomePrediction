from flask_wtf import FlaskForm
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms import StringField, SubmitField, SelectField

class DataForm(FlaskForm):
    education = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th',
                 '10th', '11th', '12th', 'Hs-grad', 'Some-college',
                 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 'Masters',
                 'Prof-school', 'Doctorate']
    country = ['United-states', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Puerto-rico', 'Honduras', 'England', 'Canada',
               'Germany', 'Iran', 'Philippines', 'Poland', 'Columbia', 'Cambodia', 'Thailand', 'Ecuador', 'Laos',
               'Taiwan', 'Haiti', 'Portugal', 'Dominican-republic', 'El-salvador', 'France', 'Guatemala', 'Italy',
               'China', 'South', 'Japan', 'Yugoslavia', 'Peru', 'Outlying-us(guam-usvi-etc)', 'Scotland',
               'Trinadad&tobago', 'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary', 'Holand-netherlands']
    occupation = ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service', 'Sales',
                  'Transport-moving', 'Farming-fishing', 'Machine-op-inspct', 'Tech-support', 'Craft-repair',
                  'Protective-serv', 'Armed-forces', 'Priv-house-serv']
    work_class = ['Private', 'State-gov', 'Federal-gov', 'Local-gov', 'Self-emp-inc', 'Self-emp-not-inc', 'Without-pay',
                  'Never-worked']
    marital_status = ['Never-married', 'Married-civ-spouse', 'Divorced',
                      'Married-spouse-absent', 'Separated', 'Married-af-spouse', 'Widowed']
    race = ['White', 'Black', 'Asian-pac-islander', 'Amer-indian-eskimo', 'Other']
    sex = ['Male', 'Female']

    Name = StringField("Fill your name")
    Age = h5fields.IntegerField("Age", widget=h5widgets.NumberInput(min=0, max=100, step=1))
    Work_Class = SelectField('Select Work class', choices=work_class)
    Education = SelectField('Select Education', choices=education)
    Marital_Status = SelectField('Select Marital Status', choices=marital_status)
    Occupation = SelectField('Select Occupation', choices=occupation)
    Race = SelectField('Select Race', choices=race)
    Sex = SelectField('Select Sex', choices=sex)
    Capital_Gain = h5fields.IntegerField("Capital Gain", widget=h5widgets.NumberInput(min=0, step=1))
    Capital_Loss = h5fields.IntegerField("Capital Loss", widget=h5widgets.NumberInput(min=0, step=1))
    Hours = h5fields.IntegerField("Weekly Hours", widget=h5widgets.NumberInput(min=0, max=100, step=1))
    Country = SelectField('Select Country', choices=country)
    submit = SubmitField(' Predict Yearly Income Salary! ')
