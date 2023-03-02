from django.contrib import admin

from .models import Paginas_Oficiales , Municipalidad_o_Localidad , Categorias , Actividades , Categoria_de_Actividad


admin.site.register( Paginas_Oficiales )
admin.site.register( Municipalidad_o_Localidad )
admin.site.register( Categorias )
admin.site.register( Categoria_de_Actividad )

@admin.register( Actividades )
class XmlAdmin( admin.ModelAdmin ):
	list_display = ( 'id' , 'id_pagina_oficial' , 'id_municipio_localidad' , 'titulo', 'creacion')
	#fields = ( 'id_user' , 'description' , 'file_xml' , 'url' )

