from django import forms

from contactus.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'Enter Your Name'}),
            'email' : forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'Enter Your Email'}),
            'subject' : forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'Enter Your Subject'}),
            'message' : forms.Textarea(attrs={'class': 'form-control','type':'text','placeholder':'Enter Your Message'}),
        }





