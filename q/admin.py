from django.contrib import admin
from .models import Post, Category, Comments, History, Regulations
# Register your models here.
class PostAdmin(admin.ModelAdmin):

   fields = ['title', 'description', 'content', 'post_cat', 'upload']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(History)
admin.site.register(Regulations)

