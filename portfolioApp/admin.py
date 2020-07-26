from django.contrib import admin
from .models import About, Skills, Portfolio, Contact, PortfolioImages

# Register your models here.

admin.site.register((About, Skills, Contact))

class PortfolioImagesAdmin(admin.StackedInline):
    model = PortfolioImages

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImagesAdmin]

    class Meta:
       model = Portfolio

@admin.register(PortfolioImages)
class PortfolioImagesAdmin(admin.ModelAdmin):
    pass
