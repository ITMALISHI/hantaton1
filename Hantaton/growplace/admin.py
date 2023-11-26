from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoryDescription)
class CategoryDescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

@admin.register(EventOrganizer)
class EventOrganizerAdmin(admin.ModelAdmin):
    pass

@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    pass








# Register your models here.
