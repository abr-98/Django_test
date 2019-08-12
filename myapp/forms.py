from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   '''the field type can take "widget" argument for html rendering; 
   in our case, we want the password to be hidden, not displayed. 
   Many others widget are present in Django: DateInput for dates, 
   CheckboxInput for checkboxes,'''


   