from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Category)