from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
    def is_phone_valid(self):
        try:
            return  Customer.objects.get(phone_no=int(self.phone_no))
        except Customer.DoesNotExist:
            return None  
            