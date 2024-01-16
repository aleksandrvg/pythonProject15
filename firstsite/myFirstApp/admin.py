from django.contrib import admin
from .models import *
class ArticeleAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'create_date')
    def create_date(self, obj):
        return obj.created

# Register your models here.
admin.site.register(Article)
admin.site.register(Customer)
admin.site.register(CustomerSettings)
admin.site.register(Publications)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)