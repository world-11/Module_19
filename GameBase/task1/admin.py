from django.contrib import admin


# Register your models here.
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title',)
    list_filter = ('size', 'cost',)
    list_per_page = 20

@admin.register(Buyer)
class BayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    list_filter = ('balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    fieldsets = (
        (None, {
        'fields': ('name', 'age')
        }),
        ('Дополнительные настройки', {
            'fields': ('balance', )
        })
    )
    readonly_fields = ('balance',)

