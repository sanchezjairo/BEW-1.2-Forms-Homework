from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, TextAreaField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    title = StringField('Title:', validators=[DataRequired(), Length(min=1, max=50)])
    address = TextAreaField('Address:', validators=[DataRequired(), Length(min=1, max=50)])
    submit = SubmitField('Submit')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name:', validators=[DataRequired(), Length(min=1, max=40)])
    price = FloatField('Price:', validators=[DataRequired()])
    category = SelectField("Category:", choices = ItemCategory.choices())
    photo_url = StringField('Photo URL:', validators=[DataRequired(), URL()])
    store = QuerySelectField('Store:', query_factory=lambda: GroceryStore.query, allow_blank=False)
    
    submit = SubmitField('Submit')
    pass

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
