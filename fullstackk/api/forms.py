from django import forms
from .models import User


# can use forms or model form(In fact if your form is going to be used to directly add or edit a Django model, a ModelForm can save you a great deal of time, effort, and code, because it will build a form, along with the appropriate fields and their attributes, from a Model class)
class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password"]
