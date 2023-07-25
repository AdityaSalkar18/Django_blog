from django.contrib import admin
from app.models import Post
from app.models import Profile
from app.models import Feedback

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Feedback)