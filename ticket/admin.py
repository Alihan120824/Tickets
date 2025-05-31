from django.contrib import admin
from django.core.paginator import Paginator

from .models import Ticket, Purchase

admin.site.register(Ticket)
admin.site.register(Purchase)
