from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customers import Customer
from django.views import View

class Signup(View):
    
    def get(self, request):
        return render(request,'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_Name = postData.get('firstname')
        last_Name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        
        #validation
        value = {
            'first_Name': first_Name,
            'last_Name': last_Name,
            'phone': phone,
            'email': email
        }
        
        error_message = None
        
        customer = Customer(first_Name = first_Name,
                             last_Name = last_Name,
                             phone = phone,
                             email = email,
                             password = password 
        )
        error_message = self.validateCustomer(customer)
        
        if not error_message:
            print(first_Name, last_Name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
        
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter Your First Name !!"
        elif len(customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        
        return error_message
        