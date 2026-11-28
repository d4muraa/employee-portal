from flask_wtf import FlaskForm
from wtforms import DateField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Masuk")


class LeaveForm(FlaskForm):
    start_date = DateField("Tanggal mulai", validators=[DataRequired()])
    end_date = DateField("Tanggal selesai", validators=[DataRequired()])
    reason = StringField("Alasan", validators=[DataRequired(), Length(max=255)])
    submit = SubmitField("Ajukan")