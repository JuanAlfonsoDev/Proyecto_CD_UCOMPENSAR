# Importaciones de las librerias 
#streamlit: Transforma scripts de python en apliciones web sin necesidad de usar lenguajes webs (HTML, CSS ,JS)
# Numpy: Sirve para realizar calculos numericos y cientificos a gran escala
# ploty: Sirve para crear graficos interactivos con sus dashboard
# Sympy: Sirve para manipular variables como (x,y) de forma exacta
# Pandas: Sirve para el analisis datos tabulares(filas y columnas)
import streamlit as web
import numpy as num
import plotly as plot 
import sympy as sym 

# FIN DE LAS IMPORTACIONES DE LAS LIBRERIAS 


# COSAS VISUALES 

web.title("Campaña publicitaria Situación 2B") # Titulo para la pagina 
web.subheader("Sistema de análisis de campañas publicitarias") # Subtitulo 
web.write("Panel interactivo para analizar los ingresos y apoyar las decisiones de mercadeo.") # Muestra parrafo en la pantalla 

# FIN DE LAS COSAS VISUALES 


# DATOS PREVIOS A TENER EN CUENTA 
 
x = num.linspace(0, 25, 100) # genera 100 valores de dias entre 0 y 25 
funcion = -2*x**2 + 80*x + 500 #  Es la funcion dada.

# FIN DATOS PREVIOS A TENER EN CUENTA  

# CONSTRUCCION DE LA 1 GRAFICA 
fig = plot.graph_objects.Figure() # CREA EL ESPACIO DEL PLANO CARTESIANO 
fig.add_trace(plot.graph_objects.Scatter(x=x, y=funcion, mode="lines", name="Ingresos diarios")) 

# x=x: los días de la campaña.
# y=funcion: los ingresos calculados.
# mode="lines": dibuja una línea continua.
# name="Ingresos diarios": asigna un nombre a la curva.


fig.update_layout(
    title="Comportamiento de los ingresos diarios de la campaña", # titulo de la grafica 
    height=500, # altura de la grafica
    width=800, # ancho de la grafica
    xaxis=dict( # Se modifica el eje x(xaxis), se crea un diccionario (dict), con los datos title(titulo), dictk(muestra los saltos en x en este cado de 1), range: el rango de vista(desde,hasta), minallowed: valor minimo de la visualizacion, maxllowed: valor maximo de la visualizacion 
        title="Días de campaña",
        dtick=1,
        range=[0, 25],
        minallowed=0,
        maxallowed=25
    ),
    yaxis=dict(  # Se modifica el eje y(yaxis), se crea un diccionario (dict), con los datos title(titulo), dictk(muestra los saltos en x en este cado de 100), range: el rango de vista(desde,hasta), minallowed: valor minimo de la visualizacion, maxllowed: valor maximo de la visualizacion 
        title="Ingresos diarios (miles de pesos)",
        dtick=100,
        range=[0, 1500],
        minallowed=0,
        maxallowed=1500
    )
)
# fig.update_layout: Permite modificar la presentacion y el deseño de la grafica 

fig.add_trace(plot.graph_objects.Scatter(
    x=[20], # Ubicamos el punto en el eje x 20 
    y=[1300], # indicamos el ingreso 1.300 miles de pesos en el eje y 
    mode="markers",  # Muestra un marcador no una linea 
    name="Máximo de ingresos" # Indica el nombe del marcador
))


web.plotly_chart(fig, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 
# FIN CONSTRUCCION DE LA 1 GRAFICA  

# Creacion de la derivada 
derivada = -4*x + 80

web.subheader("Variación de los ingresos") 

# CONSTRUCCION DE LA 2 GRAFICA
fig_derivada = plot.graph_objects.Figure() # Se crea una nueva figura vacia 
fig_derivada.add_trace(plot.graph_objects.Scatter(
    x=x,
    y=derivada,
    mode="lines",
    name="Tasa de variación"
    )
)
fig_derivada.update_layout(
    title="Tasa de variación de los ingresos", # titulo de la grafica 
    xaxis_title="Días de campaña", # titulo del eje x
    yaxis_title="Variación (miles de pesos por día)", # titulo del eje y
    height=500, # altura de la graica
    width=800 # ancho de la grafica
)

# x=x: representa los días de campaña.
# y=derivada: representa el resultado de la derivada.
# mode="lines": dibuja una línea continua.
# name="Tasa de variación": identifica la curva.
web.plotly_chart(fig_derivada, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 
# FIN DE LA CONSTRUCCION DE LA 2 GRAFICA
