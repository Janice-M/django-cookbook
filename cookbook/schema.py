#cookbook/schema.py

import graphene 
from graphene_django import DjangoObjectType
from cookbook.ingredients.models import Category, Ingredient

class CateforyType(DjangoObjectType):
    class Meta:
        model=Category
        fields = ("id", "name" ,"ingredients")