from django.contrib import admin
from .models import ExcursionTour, BeachTour, SkiTour, Presentation

class BaseTourAdmin(admin.ModelAdmin):
    def show_cost(self, obj):
        return f"{obj.calculate_cost()} Р"
    show_cost.short_description = '💰 Стоимость'

@admin.register(ExcursionTour)
class ExcersionAdmin(BaseTourAdmin):
    list_display = ['direction', 'departure_date', 'paris_excursion', 'rome_excursion', 'istanbul_excursion', 'saint_excursion', 'status']
    list_editable = ['status']
    
@admin.register(BeachTour)
class BeachAdmin(BaseTourAdmin):
    list_display = ['direction', 'departure_date', 'phuket_beach', 'hurghada_beach', 'bali_beach', 'male_beach', 'status']
    list_editable = ['status']

@admin.register(SkiTour)
class SkiAdmin(BaseTourAdmin):
    list_display = ['direction', 'departure_date']

@admin.register(Presentation)
class PresentationAdmin(BaseTourAdmin):
    list_display = ['name','surname']




