$( document ).ready(function() {
    console.log( "Documento Cargado!" );
    pinta_filtros_actividades_provincia_mendoza( { "categorias":[] , "lista_municipalidad_localidad":[] } )
    descarga_actividades_provincia_mendoza( pagina_actual );
});

function descarga_actividades_provincia_mendoza(){
    
    // ----------- Filtros para la busqueda --------->>>>>>>>
    let filtro_municipalidad = $("#filtro_select_municipalidad").val();
    let filtro_categoria = $("#filtro_select_categoria").val();
    // ---------------------------------------------->>>>>>>>
    console.log( "Pagina actual: " + pagina_actual )
    $.ajax({
        headers: {'X-CSRFToken': CSRF_TOKEN} ,
        url: url_api_actividades_provincia_mendoza ,
        type:'post',
        data:{
            "filtro_municipalidad":filtro_municipalidad,
            "filtro_categoria":filtro_categoria,
            "actividad_inicial":pagina_actual*30,
            "actividad_final":pagina_actual*30+30
            },
        dataType:'JSON',
        success: function( request ){
            console.log( request )
            pinta_datos_actividades_provincia_mendoza( request["actividades"] )
            if (primera_carga == false){
                pinta_filtros_actividades_provincia_mendoza( request )
                primera_carga = true
            }
        },
        error: function( request ){
            console.log("Error Error Error")
        },
    })
    
}

function pinta_datos_actividades_provincia_mendoza( json_actividades ){
    
    lista_divs_historial.forEach( divs_ingresados => {
        divs_ingresados.remove()
    });
    
    lista_divs_historial = []
    
    json_actividades.reverse().forEach( actividad_mendoza => {

        let div_actividad_mendoza = $("#div_actividad_mendoza").clone()
        $(div_actividad_mendoza).attr("hidden",false)

        $(div_actividad_mendoza).find("img").attr("src", actividad_mendoza["link_imagen"] )
        
        $(div_actividad_mendoza).find("#Titulo_nota").text( actividad_mendoza["titulo"] )
        $(div_actividad_mendoza).find("#Subtitulo_nota").text( actividad_mendoza["texto_nota"] )

        $(div_actividad_mendoza).find("#categorias").text( "Categoria: "+ actividad_mendoza["categorias"] )

        actividad_mendoza["creacion"] = actividad_mendoza["creacion"].replace('T00:00:00Z', '')
        $(div_actividad_mendoza).find("#creacion").text( "Fecha: "+ actividad_mendoza["creacion"] )
        
        $(div_actividad_mendoza).find("#municipio_localidad").text( "Municipio Localidad: "+ actividad_mendoza["municipio_localidad"] )

        $(div_actividad_mendoza).find("#link_nota_original").attr("href", actividad_mendoza["link_nota_original"])
        
        /*
        $(div_actividad_mendoza).find("#fecha_creacion").text( String('Fecha Creacion: ' + xml_data["fecha_creacion"] ) )
        */
        $( div_actividad_mendoza ).insertBefore("#div_actividad_mendoza")
        
        lista_divs_historial.push( div_actividad_mendoza )

    }); 
}

function pinta_filtros_actividades_provincia_mendoza( request_data ){
    $('#filtro_select_categoria')[0].options.length = 0;
    $('#filtro_select_municipalidad')[0].options.length = 0;

    $('#filtro_select_categoria').append( new Option( "Todas" , -1 ) );
    request_data["categorias"].forEach( categoria_json => {
        $('#filtro_select_categoria').append( new Option( categoria_json["nombre"] , categoria_json["id"] ) );
    });

    $('#filtro_select_municipalidad').append( new Option( "Todas" , -1 ) );
    request_data["lista_municipalidad_localidad"].forEach( muni_local_json => {
        $('#filtro_select_municipalidad').append( new Option( muni_local_json["nombre"] , muni_local_json["id"] ) );
    });
}

function cambiando_de_numero_pagina( numero_pagina ){
    if (numero_pagina !== pagina_actual){
        pagina_actual = numero_pagina
        $("#numero_pagina_actual").text( "Pagina: " + String(pagina_actual) )
        descarga_actividades_provincia_mendoza()
        window.scroll( 0, 0)
    }
}