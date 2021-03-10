from django import forms
from .models import Customer

software_list = plan_type = [('Web Application','Web Application'), ('Mobile Application','Mobile Application'), ('Desktop Application','Desktop Application'),
                             ('Chatbot','Chatbot'), ('Web Crawler','Web Crawler'), ('Others','Others')]
category_list = [('Personal Project','Personal Project'), ('Business Project','Business Project'), ('Academic/School Project','Academic/School Project'),
                 ('Research Project','Research Project'), ('Others','Others')]

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Fullname', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="Full Name")
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Email Address', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="Email Address")
    phone_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Enter Phone No', 'class': 'form-control mb-4', 'id': 'inputUsername'}),
        label="Phone Number")
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter Project Details (brief)', 'class': 'form-control mb-4', 'id': 'inputUsername', 'required': 'False'}),
        label="Details")
    software_type = forms.CharField(
        widget=forms.Select(attrs={'placeholder': 'Select Software Type', 'class': 'form-control mb-4', 'id': 'inputUsername'},
                            choices=software_list), label="Software Type")
    category = forms.CharField(
        widget=forms.Select(
            attrs={'placeholder': 'Select Category', 'class': 'form-control mb-4', 'id': 'inputUsername'},
            choices=category_list), label="Category")

    """def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['details'].required = False """