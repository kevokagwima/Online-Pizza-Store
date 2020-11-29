from django.contrib import admin

from .models import dinner_platters, pasta, regular_pizza, salads, silican_pizza, subs, toppings
# Register your models here.
admin.site.register(toppings)
admin.site.register(pasta)
admin.site.register(salads)
admin.site.register(regular_pizza)
admin.site.register(silican_pizza)
admin.site.register(subs)
admin.site.register(dinner_platters)
