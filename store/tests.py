from django.test import TestCase, Client
from store.models.customers import Customer

# Create your tests here.
#test
#1. test_customer_creation(self):
##
class  CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.client = Client()
        cls.first_name = Customer.objects.create(first_name='John')
        cls.last_name = Customer.objects.create(last_name = 'Doe')
        cls.phone_no = Customer.objects.create(phone_no= 1234567890)
        cls.email = Customer.objects.create(email= "johndoe@gmail.com")
        cls.password = Customer.objects.create(password = "myPassword")
        return super().setUpTestData()
    
    def test_first_name_content(self):
        """
        The first name field must be filled with the content of John.
        """
        self.assertEqual(f"{self.first_name}", "John")
        
    def test_phone_number_is_valid(self):
        """
        The phone number should contain only numbers and it's length should be equal to or greater than 10.
        """
        valid_phone = Customer(phone_no= 1234567890)
        invalid_phone = Customer(phone_no="abcdefg")
        too_short_phone = Customer(phone_no="123")

        self.assertTrue(valid_phone.is_phone_valid())
        self.assertFalse(invalid_phone.is_phone_valid())
        self.assertFalse(too_short_phone.is_phone_valid())  
   