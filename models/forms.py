from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired
class CredCarForm(FlaskForm):
    cardHolder = StringField("cardHolder", validators=[DataRequired()])
    cardNumber = StringField("cardNumber",  validators=[DataRequired()])
    validThru = DateField("validThru", validators=[DataRequired()])
    options = SelectField('Select Validation', choices=[('start_with', 'start with a 4, 5 or 6'),
                                                        ('exactly16', 'contain exactly 16 digits'),
                                                        ('digits', 'consist of digits (0-9)'),
                                                        ('group4','have digits in groups of 4, separated by one hyphen -'),
                                                        ('separator',"NOT use any other separator like ' ' , '_'"),
                                                        ('consecutive','NOT have 4 or more consecutive repeated digit')])
    result = StringField("result")
    submit = SubmitField('Submit')




