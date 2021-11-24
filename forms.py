from django import forms



class log(forms.Form):
    name=forms.CharField(max_length=50)
    username=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=50)

class adminform(forms.Form):
    name=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)


class emploe(forms.Form):
    emp_no=forms.CharField(max_length=50)
    desg=forms.CharField(max_length=50)
    fname=forms.CharField(max_length=50) 
    lname=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)
    adrs1=forms.CharField(max_length=50)
    adrs2=forms.CharField(max_length=50)
    city=forms.CharField(max_length=50)
    pin=forms.CharField(max_length=50)
    state=forms.CharField(max_length=50)
    depart2=forms.CharField(max_length=50)
    
