from django.contrib import admin
from .models import Categorystay, Baby,Sitter,Item,Pay

# Register your models here.
admin.site.register(Categorystay)
admin.site.register(Baby)
admin.site.register(Sitter)
admin.site.register(Pay)
admin.site.register(Item)