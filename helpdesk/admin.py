from django.contrib import admin
from .models import Ticket, Comment, Category, CustomUser

admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(CustomUser)


# Register your models here.
