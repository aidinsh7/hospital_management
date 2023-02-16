from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        widget ={ 'booking_date':DateInput()}
        lable = {
            'p_name' : 'Patient Name',
            'p_phone' : 'Patient Phone',
            'p_email' :'Patient Email',
            'doc_name' :'Doctor Name',
            'booking_date' : 'Booking Date',
            'p_image' : 'Patient Image',
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        lable = {
            'doc_name': 'Doctor Name',
            'doc_spec': 'Specialization',
            'doc_image': 'Doctor Image',
            'department_name': 'Department Name',

        }


class DoctorAddforms(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        labels = {
            'doc_name': 'Doctor Name',
            'doc_spec': 'Specialization',
            'dep_name': 'Department',
            'doc_img': 'Booking Date',
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ('username','email','password1','password2')

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        useremail = self.cleaned_data['email']
        if commit:
            user.commit
        return user
















