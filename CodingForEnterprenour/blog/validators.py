from django.core.validators import ValidationError



def email_validator(value):
    if '@' not in value:
        raise ValidationError('Not a valid email')
    else:
        return value