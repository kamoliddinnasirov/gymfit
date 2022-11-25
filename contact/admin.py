from django.contrib import admin
from contact.models import ContactBannerModel, ContactModel

@admin.register(ContactBannerModel)
class ContactBanner(admin.ModelAdmin):
    list_display = ('contact_title', 'created_at')
    list_display_links = ('contact_title',)
    list_filter = ('created_at',)


@admin.register(ContactModel)
class Contact(admin.ModelAdmin):
    list_display = ('phone', 'email', 'location')
    list_display_link = ('phone', 'email', 'location')
    list_filter = ('created_at',)
