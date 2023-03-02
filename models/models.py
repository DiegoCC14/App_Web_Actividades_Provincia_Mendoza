from django.db import models

class Paginas_Oficiales(models.Model):
	id = models.AutoField( primary_key=True )
	nombre = models.CharField( max_length=100 )
	link_pagina = models.CharField( max_length=200 )

class Municipalidad_o_Localidad(models.Model):
	id = models.AutoField( primary_key=True )
	nombre = models.CharField(max_length=200)

class Categorias(models.Model):
	id = models.AutoField( primary_key=True )
	nombre = models.CharField(max_length=200)

class Actividades(models.Model):
	id = models.AutoField( primary_key=True )
	id_pagina_oficial = models.ForeignKey( Paginas_Oficiales , on_delete=models.CASCADE )
	id_municipio_localidad = models.ForeignKey( Municipalidad_o_Localidad , on_delete=models.CASCADE )
	titulo = models.CharField(max_length=300)
	texto_nota = models.CharField(max_length=300)
	link_nota_original = models.CharField(max_length=300)
	link_imagen = models.CharField(max_length=300)
	creacion = models.DateTimeField(max_length=300)




class Categoria_de_Actividad(models.Model):
	id = models.AutoField( primary_key=True )
	id_actividad = models.ForeignKey( Actividades , on_delete=models.CASCADE )
	id_categoria = models.ForeignKey( Categorias , on_delete=models.CASCADE )

