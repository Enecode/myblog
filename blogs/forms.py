from django import forms


class Form(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    services = forms.CharField(max_length=150)
    text = forms.TextInput
    phone = forms.IntegerField()
    email = forms.EmailField()

    def __str__(self):
        return self.text
