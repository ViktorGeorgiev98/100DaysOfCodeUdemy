from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email
import re
from wtforms.validators import ValidationError


class Form_Login(FlaskForm):
    email = EmailField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired()])
    login = SubmitField("Login")

    """
    Custom validation
    Because we use the format 'validate_<field_name>'
    the function will be called automatically when the form is validated.
    It gets automatically detected by flask
    """

    def validate_password(self, field):
        password = field.data
        if not re.search(r"[A-Z]", password):  # At least one uppercase letter
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[a-z]", password):  # At least one lowercase letter
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )
        if not re.search(r"[0-9]", password):  # At least one number
            raise ValidationError("Password must contain at least one number.")
        if not re.search(
            r"[!@#$%^&*(),.?\":{}|<>]", password
        ):  # At least one special character
            raise ValidationError(
                "Password must contain at least one special character."
            )
        if len(password) < 8:  # Minimum length of 8 characters
            raise ValidationError("Password must be at least 8 characters long.")
