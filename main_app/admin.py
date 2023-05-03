from django.contrib import admin

# Register your models here.
from .models import Circle, Comment
admin.site.register(Circle)
admin.site.register(Comment)