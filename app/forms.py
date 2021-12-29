from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    tittle = StringField("tittle", validators=[DataRequired()])
    author = StringField("author", validators=[DataRequired()])
    rental = StringField("rental", validators=[DataRequired()])