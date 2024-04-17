from django.db import models

from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,ActivatorModel,TitleDescriptionModel
)

class Contact(TimeStampedModel,ActivatorModel,TitleDescriptionModel,Model):
    

    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name_plural="Contacts"
    
    def __str__(self) -> str:
        return f'{self.title}'


