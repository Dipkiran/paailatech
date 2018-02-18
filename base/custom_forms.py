from django import forms

name_error={
    'required': 'Your name is required',
    'invalid': 'Invalid name'
}

email_error= {
    'required': 'Your email is required',
    'invalid': 'Invalid email'
}

message_error={
    'required': 'Please enter a message',
}

integer_error_message = {
    'required': 'Please check your phone number for possible errors',
    'invalid': 'Enter a valid number'
}


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, error_messages=name_error)
    email = forms.EmailField(required=True, error_messages=email_error)
    message = forms.CharField(required=True, error_messages=message_error, widget= forms.Textarea)


class ApplicationForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, error_messages=name_error)
    email = forms.EmailField(required=True, error_messages=email_error)
    doc = forms.FileField()
