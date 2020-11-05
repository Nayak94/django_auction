from django import forms
from .models import Client
from .models import Sinfo

# For adding widgets in forms , add a field in forms called widget. This is only for forms , not modelforms
#widget = forms.Textarea
#widget = forms.PasswordInput
#widget = forms.CheckboxSelectMultiple

# to use wigets in modelforms , add a variable as widgets = { key : form.widgetname}

# class RegisterForm(forms.Form):
#     SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
#     fname = forms.CharField(label='First Name', max_length=100)
#     lname = forms.CharField(label='Last Name', max_length=100)
#     mailid = forms.EmailField(label='Email', max_length=100)
#     sex = forms.ChoiceField(label='Sex', choices=SEX_CHOICES)
#     age = forms.IntegerField(label='Age', choices=SEX_CHOICES)
#
#


class AuthForm(forms.ModelForm):
    # fname = forms.CharField(label='First Name', max_length=100)
    # lname = forms.CharField(label='Last Name', max_length=100)
    # mailid = forms.EmailField(label='Email', max_length=100)
    class Meta:
        model = Client
        fields = ['fname', 'lname', 'mailid']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mailid': 'Email',
        }


class RegisterForm(forms.ModelForm):

    # if you want to refer a choice field directly from model . Note , the parameter that you are referring should be there in the model
    #Note :- This is referring
    # sex = forms.ModelChoiceField(queryset=Client.objects,
    #                             empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Client
        fields = ['fname', 'lname', 'mailid', 'sex', 'age']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mailid': 'Email',
            'sex': 'Sex',
            'age': 'Age'
        }
        #widgets = {'sex': forms.RadioSelect}


class ItemForm(forms.Form):
    number = forms.IntegerField(min_value=0, max_value=6)


class ItemRegisterForm(forms.ModelForm):

    class Meta:
        model = Sinfo
        fields = ['iname', 'idesc']
        labels = {
            'iname': 'Item Name',
            'idesc': 'Description'
        }
