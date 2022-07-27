from django.contrib import admin
from .models import *

class detReleaseMachine(admin.ModelAdmin):
    list_display = ('id', 'date', 'hour', 'idMachineFK','idAssociateFK')
    list_display_links = ('id',)
    search_fields = ('idMachineFK','idAssociateFK')
    list_per_page = 10

admin.site.register(ReleaseMachine, detReleaseMachine)

class detUser(admin.ModelAdmin):
    list_display = ('id', 'name', 'EDV')
    list_display_links = ('id',)
    search_fields = ('EDV')
    list_per_page = 10

admin.site.register(User, detUser)

class detApprentice(admin.ModelAdmin):
    list_display = ('id', 'name', 'EDV')
    list_display_links = ('id',)
    search_fields = ('EDV')
    list_per_page = 10

admin.site.register(Apprentice, detApprentice)

class detTypeAssociente(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id',)
    search_fields = ('type')
    list_per_page = 10

admin.site.register(typeAssociente, detTypeAssociente)

class detAssociate(admin.ModelAdmin):
    list_display = ('id', 'type', 'idAssociateFK')
    list_display_links = ('id',)
    search_fields = ('idAssociateFK')
    list_per_page = 10

admin.site.register(Associate, detAssociate)

class detMachine(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'ipaddress')
    list_display_links = ('id',)
    search_fields = ('name')
    list_per_page = 10

admin.site.register(Machine, detMachine)

class detQuestion(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id',)
    search_fields = ('type')
    list_per_page = 10

admin.site.register(Question, detQuestion)

class detGreenBook(admin.ModelAdmin):
    list_display = ('id', 'idMachineFK', 'typeQuestion','question')
    list_display_links = ('id',)
    search_fields = ('idMachineFK')
    list_per_page = 10

admin.site.register(GreenBook, detGreenBook)

class detMaintenance(admin.ModelAdmin):
    list_display = ('id', 'date', 'hour','idMachineFK', 'idAssociateFK')
    list_display_links = ('id',)
    search_fields = ('idMachineFK')
    list_per_page = 10

admin.site.register(Maintenance, detMaintenance)

