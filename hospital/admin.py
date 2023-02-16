from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('id','p_name','p_phone','p_email','doc_name','p_image','booking_on','booking_date')
    list_display_links = ('id','p_name','p_email','p_phone','doc_name','booking_date','booking_on')
    list_filter = ('p_name','p_phone','p_email','doc_name','booking_date','booking_on')
    search_fields = ('p_name','p_phone','p_email','doc_name','booking_date','booking_on')
    list_per_page = 30

admin.site.register(Booking,BookingAdmin)