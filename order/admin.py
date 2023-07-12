from django.contrib import admin
from .models import Order, OrderDetail

# Register your models here.

#class OrderAdmin(admin.ModelAdmin):
#    readonly_fields = ('created')

#admin.site.register(Order, OrderAdmin)

#class OrderDatailAdmin(admin.ModelAdmin):
#    readonly_fields = ('created')

#admin.site.register(OrderDetail, OrderDetailAdmin)

admin.site.register([Order, OrderDetail])