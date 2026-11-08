from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Pet_Store(AbstractUser):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email1=models.CharField(max_length=20)
    phone1=models.CharField(max_length=15)
    address1=models.CharField(max_length=100)

    
class PetManager(models.Manager):
    def search(self,query):
        if query:
            return self.get_queryset().filter(models.Q(name__exact = query))

class Pet(models.Model):
    name=models.CharField(max_length=30,validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$',
                                                    message=("Name can contain only alphabets and spaces"),
                                                    code="invalid name")])
    breed=models.CharField(max_length=30)
    age=models.IntegerField(validators=[MinValueValidator(1,message=("The minimum age value for pet is 1 years")),
                                MaxValueValidator(15,message=("The maximum age for pet is 15 years"))])
    price=models.DecimalField(max_digits=10, decimal_places=2,
                            validators=[MinValueValidator(10000,message=("The minimum price pet should be 10k"))])
    type=models.CharField(max_length=10)
    description=models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_images/')
    
    objects = PetManager()

    
    class Meta:
        permissions = [
            ('can_add_pet','can add a pet'),
            ('can_update_pet','can update a pet'),
            ('can_delete_pet','can delete a pet'),
            ('can_add_pet_products','can add a pet_product'),
            ('can_update_pet_products','can update a pet_product'),
            ('can_delete_pet_products','can delete a product_product')
        ]
        

class Pet_products(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator
                                        (1000,message=("The minimum price pet product should be 10k"))])
    quantity_in_stock = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    

class Order(models.Model):
    user_id = models.ForeignKey(Pet_Store, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    payment_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS_CHOICES, default='PENDING'
    )
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Pet_products, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    
class Cart(models.Model):
    customer_id = models.ForeignKey(Pet_Store,on_delete=models.CASCADE)
    pet_id = models.ForeignKey(Pet,on_delete=models.CASCADE ,null= True, blank= True) 
    product_id = models.ForeignKey(Pet_products,on_delete=models.CASCADE,null= True, blank= True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField()
    

class Payments(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

