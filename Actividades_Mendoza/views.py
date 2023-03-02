from pathlib import Path
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from models.models import Categorias , Paginas_Oficiales , Municipalidad_o_Localidad , Actividades , Categoria_de_Actividad

BASE_DIR = Path(__file__).resolve().parent.parent


class Actividades_Provincial_Mendoza( View ):
	
	def get( self , request ):
		return render( request , 'home.html' )


class API_Actividades_Provincia_Mendoza( View ):

	def post( self , request ):
		lista_actividades = []
		data_request = request.POST.dict()
		
		#lista_categorias
		lista_categorias = [ { "id":obj_categoria.id , "nombre":obj_categoria.nombre } for obj_categoria in Categorias.objects.all() ]
		#================

		#lista_municipalidad_localidad
		lista_municipalidad_localidad = [ { "id":obj_munilocal.id , "nombre":obj_munilocal.nombre } for obj_munilocal in Municipalidad_o_Localidad.objects.all() ]
		#================

		#Dependiendo de los filtros agregados la consulta cambiara
		print(f"Filtro Municipalidad: {data_request['filtro_municipalidad']}")
		print(f"Filtro Categoria: {data_request['filtro_categoria']}")
		if data_request['filtro_municipalidad'] == "-1": #-1 es Todas
			list_object_actividades = Actividades.objects.all().order_by('-creacion')
		else:
			list_object_actividades = Actividades.objects.filter( id_municipio_localidad__id=data_request['filtro_municipalidad'] ).order_by('-creacion')
		
		if data_request['filtro_categoria'] != "-1": #-1 es Todas
			lista_obj_actividad_categoria = Categoria_de_Actividad.objects.filter( id_categoria=data_request['filtro_categoria'] )
			list_object_actividades = list_object_actividades.filter( id__in=[ obj_act_categorita.id_actividad.id for obj_act_categorita in lista_obj_actividad_categoria] ).order_by('-creacion')
		
		list_object_actividades = list_object_actividades[ int(data_request["actividad_inicial"]): int(data_request["actividad_final"]) ]
		#==============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

		#Serializando ----------->>>>>>>>>>>
		for obj_actividad in list_object_actividades:
			# id_pagina_oficial = models.ForeignKey( Paginas_Oficiales , on_delete=models.CASCADE )
			actividad_json = {
				"titulo" : obj_actividad.titulo ,
				"texto_nota" : obj_actividad.texto_nota ,
				"link_nota_original" : obj_actividad.link_nota_original ,
				"link_imagen" : obj_actividad.link_imagen ,
				"creacion" : obj_actividad.creacion,
				"categorias" : Categoria_de_Actividad.objects.filter( id_actividad=obj_actividad )[0].id_categoria.nombre,
				"municipio_localidad" : obj_actividad.id_municipio_localidad.nombre,
			}
			lista_actividades.append( actividad_json )

		#=============----------->>>>>>>>>>>

		return JsonResponse( {"actividades":lista_actividades , "categorias":lista_categorias , "lista_municipalidad_localidad":lista_municipalidad_localidad} )