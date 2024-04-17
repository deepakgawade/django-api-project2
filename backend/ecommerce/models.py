from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from utils.model_abstracts import Model

from django_extensions.db.models import (
    TimeStampedModel,ActivatorModel,TitleDescriptionModel

)
User = settings.AUTH_USER_MODEL
class Item(
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
    Model
    ):
    
    """
    ecommerce.Item
    stores Item in our shop
    """

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ["id"]

    def __str__(self):
        return self.title
    
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    
    def amount(self):
        #convert price from pence to pounds
        amount=float(self.price/100)
        return amount
    
    def manage_stock(self, qty):
        #this will remove items from store as they are sold
        new_stock=self.stock-int(qty)
        self.stock=new_stock
        self.save()

    def check_stock(self,qty):
        #if items exist in store
        if int(qty)>self.stock:
            return False
        return True
    
    def place_order(self,user,qty):
        #use to place a order

        if self.check_stock(qty):
            order = Order.objects.create(item=self,
                                         quantity=qty,
                                         user=user)
            self.manage_stock(qty)
            return order
        else:
            return None






class Order(TimeStampedModel,ActivatorModel,Model):

    """

    ecommerce.Order
    stores a single order entry, related to 
    :mode:eccomerce.item and :model: auth.User

    """

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering=["id"]

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Item, null=True,blank=True,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.item.title}'
    




