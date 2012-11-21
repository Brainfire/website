from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'eight', 'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'eight', 'placeholder': 'Email'}))
    website = forms.URLField(required=False, widget=forms.TextInput(attrs={'class':'eight', 'placeholder': 'Website'}))
    
    BUDGET_CHOICES = (
        ('$1000 - $5000','$1000 - $5000'),
        ('$5,000 - $10,000','$5,000 - $10,000'),
        ('$10,000 +','$10,000 +'),
    )
    budget = forms.ChoiceField(widget=forms.Select(attrs={'class':'four'}), choices=BUDGET_CHOICES, required=True)
    
    TIMEFRAME_CHOICES = (
        ('1 month','1 month'),
        ('1 - 3 months','1 - 3 months'),
        ('6 months +','6 months +'),
    )
    timeframe = forms.ChoiceField(widget=forms.Select(attrs={'class':'four'}), choices=TIMEFRAME_CHOICES, required=True)
    
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'ten', 'placeholder': 'Your Message'}), required=True)
    
    def send_email(self):
        email_body = "Name: {} \nWebsite: {}\nBudget: {}\nTimeframe: {}\nMessage: {}".format(self.cleaned_data['name'],
                                                                                                self.cleaned_data['website'], 
                                                                                                self.cleaned_data['budget'], 
                                                                                                self.cleaned_data['timeframe'], 
                                                                                                self.cleaned_data['message'])
                                            
        send_mail("Website Contact Form", email_body, self.cleaned_data['email'], ['contact@brainfi.re'])
