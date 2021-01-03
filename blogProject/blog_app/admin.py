from django.contrib import admin
from .models import Post
#admin.site.register(Post)  #Esto ya podria dejarlo de usar asi y ponerlo como lo pongo en la siguiente linea
@admin.register(Post)
#En esta linea de abajo digo que atributos quiero que se vean en la lista horizontal  donde tengo la lista de post hechos
class PostAdmin(admin.ModelAdmin):
 list_display = ('title', 'slug', 'author', 'publish', 'status')

# Pongo la lista de filtros de la derecha
 list_filter = ('status', 'created', 'publish', 'author')
 search_fields = ('title', 'body')
 prepopulated_fields = {'slug': ('title',)}
 raw_id_fields = ('author',)
 date_hierarchy = 'publish'
 ordering = ('status', 'publish')