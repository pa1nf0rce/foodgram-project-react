from django.contrib import admin
from users.models import CustomUser, Follow

admin.site.register(CustomUser)
admin.site.register(Follow)
