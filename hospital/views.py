from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *



# Create your views here.

def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')


def bookings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =BookingForm(request.Post,request.FIELS)
            if form.is_valid():
                form.save()
                return render(request,'confrm.html')
            else:
                dict_form = BookingForm(
                    form = {'form':form}
                )
                return render(request, 'booking.html',dict_form)
        else:
            messages.success(request,'you are need to login for booking')
            return redirect('login')
        messages.error(request,'somthink is wrong try again')
        return redirect('login')



def viewbooking(request):
    if request.user.is_supereuser:
        dict_viewbooking = {
            'bookings': Booking.objects.all()
        }
        return render(request,'viewbooking.html',dict_viewbooking)
    else :
        messages.error(request, "You are not authorized to view this page")
        return redirect("login")



def doctors(request):
    dict_doctors= {
        'doctors':Doctor.objects.all()

    }
    return  render(request,'doctors.html',dict_doctors)


def add_doctors(request):
    if request.user.is_authenticated:
        form = DoctorAddforms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'confrm.html')
        else:
            form = DoctorAddforms
            dict_form={
                'form':DoctorAddforms
            }
            return render(request,'adddocters.html',dict_form)



def department(request):
    dict_department = {
        'department':Department.objects.all()

    }
    return  render(request,'department.html',dict_department)


def bookings(request):
    dict_bookings = {
        'bookings':Booking.objects.all().values('p_name','p_phone','doc_name','booking_date')
    }
    return render(request,'viewbooking.html',dict_bookings)




class NewUser(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



def register(request):
    if request.method == 'POST':
        form = NewUserForm()
        if form.is_valid():
            form = form.save()
            messages.success(request,'successfull registeration ,please login')
            return  redirect('login')
        else:
            messages.error(request,'invalid information')
            return redirect('register')
        messages.error(request, 'invalid information')
        return redirect('register')





def login_view(request):
     if request.method =='POST':
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_date.get('username')
            password =form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,User)
                return redirect('profile')
            else:
                messages.error(request,'invalid user or password ')
                return redirect('login')
        form = AuthenticationForm()
        return render(request,'login.html',{'login_form':form})


def logout_view(request):
    if User.is_authenticated:
      logout(request)
      messages.success(request,'you are loggedout')
      return redirect('login')
    



def profile(request):
     if request.user.is_authenticated:
         return render(request,'profile.html')
     else:
         return redirect('login')


