from django.core.exceptions import ValidationError



def validate_email(value):
    if not '@' in value:
        raise ValidationError("Not a valid email")
    return value

def validate_title(value):
    not_allowed_words = ['blah', 'testing', 'wasting time']
    value_arr = value.split()
    
    for word in value_arr:
        if word in not_allowed_words:
            raise ValidationError('%s word is not allowed'%word)
    
    return value
