from django.contrib import admin

# Register your models here.

from administrator.models import Category, Product, Developer, Publisher
from accounts.models import User

admin.site.register([Category, Product, Developer, Publisher, User])