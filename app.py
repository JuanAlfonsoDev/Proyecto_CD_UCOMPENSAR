# Importaciones de las librerias 
#streamlit: Transforma scripts de python en apliciones web sin necesidad de usar lenguajes webs (HTML, CSS ,JS)
# Numpy: Sirve para realizar calculos numericos y cientificos a gran escala
# ploty: Sirve para crear graficos interactivos con sus dashboard
# Sympy: Sirve para manipular variables como (x,y) de forma exacta
# Pandas: Sirve para el analisis datos tabulares(filas y columnas)
# python -m streamlit run app.py
import streamlit as web
import numpy as num
import plotly as plot 
import sympy as sym 

# FIN DE LAS IMPORTACIONES DE LAS LIBRERIAS 


# COSAS VISUALES 

web.title("Campaña publicitaria Situación 2B") # Titulo para la pagina 
web.subheader("Sistema de análisis de campañas publicitarias") # Subtitulo 
web.write("Panel interactivo para analizar los ingresos y apoyar las decisiones de mercadeo.") # Muestra parrafo en la pantalla 

dia_seleccionado = web.slider( # Slider
    "Selecciona el día de la campaña",
    min_value=0, # valor minimo 
    max_value=25, # valor maximo 
    value=10, # valor por defecto 
    step=1 # saltos
)

ingreso_dia = -2*dia_seleccionado**2 + 80*dia_seleccionado + 500 # Formula segun el dia
tasa_variacion = -4*dia_seleccionado + 80 # Formula de la derivada segun el dia

# Analizamos el comportamiento de los ingresos según el día seleccionado, respecto al dia selecionado da una informacion 
if tasa_variacion > 0:
    interpretacion = "Los ingresos diarios están aumentando." # Si la tasa de var

elif tasa_variacion == 0:
    interpretacion = "Se alcanza el máximo de ingresos diarios."

else:
    interpretacion = "Los ingresos diarios están disminuyendo."




# Generamos una recomendación según el comportamiento de los ingresos
if tasa_variacion > 0:
    recomendacion = "La campaña presenta un crecimiento de los ingresos diarios. Se recomienda mantener el seguimiento de su rendimiento."

elif tasa_variacion == 0:
    recomendacion = "La campaña alcanza su máximo ingreso diario. Es un momento clave para evaluar su rendimiento."

else:
    recomendacion = "Los ingresos diarios están disminuyendo. Se recomienda evaluar la continuidad y efectividad de la campaña."




# FIN DE LAS COSAS VISUALES 


# DATOS PREVIOS A TENER EN CUENTA 
 
x = num.linspace(0, 25, 100) # genera 100 valores de dias entre 0 y 25 
funcion = -2*x**2 + 80*x + 500 #  Es la funcion dada.
x2 = num.linspace(25, 60, 100) # Genra 100 valores de dias entre 25 y 60 
funcion2 = 1350 - 15*(x2 - 25)# Es la segunda funcion 

# FIN DATOS PREVIOS A TENER EN CUENTA  

# CONSTRUCCION DE LA 1 GRAFICA 
fig = plot.graph_objects.Figure() # CREA EL ESPACIO DEL PLANO CARTESIANO 
fig.add_trace(plot.graph_objects.Scatter(
    x=x, # x=x: los días de la campaña.
    y=funcion, # y=funcion: los ingresos calculados.
    mode="lines", # mode="lines": dibuja una línea continua.
    name="Ingresos diarios", # name="Ingresos diarios": asigna un nombre a la curva.
    line=dict(color="#00bfa6", width=3) # Color de la linea 

    )) 

fig.add_trace(plot.graph_objects.Scatter(
    x=x2, # x = x2 los valores de 25 a 60 
    y=funcion2, #y = funcion2 para los valores cuando x2 cambie
    mode="lines", # Dibuja una linea continua
    name="Segunda fase", 
    line=dict(color="#FF9800", width=3)
))


fig.update_layout(
    title="Comportamiento de los ingresos diarios de la campaña", # titulo de la grafica 
    height=500, # altura de la grafica
    width=800, # ancho de la grafica
    xaxis=dict( # Se modifica el eje x(xaxis), se crea un diccionario (dict),    
        title="Días de campaña",  # con los datos title(titulo),
        dtick=1, # dictk(muestra los saltos en x en este cado de 1),
        range=[0, 25], # range: el rango de vista(desde,hasta),
        minallowed=0, #minallowed: valor minimo de la visualizacion,
        maxallowed=25 #  maxllowed: valor maximo de la visualizacion
    ),
    yaxis=dict(  # Se modifica el eje y(yaxis), se crea un diccionario (dict),  range: el rango de vista(desde,hasta), 
        title="Ingresos diarios (miles de pesos)", # con los datos title(titulo)
        dtick=100, # dictk(muestra los saltos en x en este cado de 100),
        range=[0, 2000], # range: el rango de vista(desde,hasta), 
        minallowed=0, # minallowed: valor minimo de la visualizacion,
        maxallowed=2000 # maxllowed: valor maximo de la visualizacion 
    )
)
# fig.update_layout: Permite modificar la presentacion y el deseño de la grafica 

fig.add_trace(plot.graph_objects.Scatter(
    x=[dia_seleccionado], # Ubicamos el punto del usuario en x
    y=[ingreso_dia], # indicamos el ingreso segun x de pesos en el eje y 
    mode="markers",  # Muestra un marcador no una linea 
    name="Día seleccionado", # Indica el nombe del marcador
    marker=dict(color="#FF5722", size=12) # Colo del punto maximo
))



# FIN CONSTRUCCION DE LA 1 GRAFICA  

# Creacion de la derivada 
derivada = -4*x + 80

web.subheader("Variación de los ingresos") 

# CONSTRUCCION DE LA 2 GRAFICA
fig_derivada = plot.graph_objects.Figure() # Se crea una nueva figura vacia 
fig_derivada.add_trace(plot.graph_objects.Scatter(
    x=x, # Valores en x de la grafica 
    y=derivada, # valores en y de la grafica 
    mode="lines", # linea continua 
    name="Tasa de variación", # titulo de la grafica 
    line=dict(color="#00bfa6", width=3) # Color de la linea 
    )


)
fig_derivada.update_layout(
    title="Tasa de variación de los ingresos", # titulo de la grafica 
    height=500, # altura de la graica
    width=800, # ancho de la grafica
    xaxis=dict(
        title="Días de campaña", #Titulo de x
        dtick=1, # dictk(muestra los saltos en x en este cado de 1),
        range=[0, 25], # range: el rango de vista(desde,hasta),
        minallowed=0, #minallowed: valor minimo de la visualizacion,
        maxallowed=25 #  maxllowed: valor maximo de la visualizacion
    ),
    yaxis=dict(
        title="Variación (miles de pesos por día)", # titulo del eje y"
        dtick=10, # dictk(muestra los saltos en x en este cado de 1),
        range=[-20, 80], # range: el rango de vista(desde,hasta),
        minallowed= -20, #minallowed: valor minimo de la visualizacion,
        maxallowed= 80 #  maxllowed: valor maximo de la visualizacion
    )
)
fig_derivada.add_trace(plot.graph_objects.Scatter( # Punto critico de la derivada
    x=[dia_seleccionado],  # Punto cricio en x 
    y=[tasa_variacion], # Punto cricio en y
    mode="markers", # Muestra un marcador no una linea
    name="Punto crítico: día 20", # Indica el nombe del marcador
    marker=dict(color="#FF5722", size=12) # Color del punto critico
))
# FIN DE LA CONSTRUCCION DE LA 2 GRAFICA


# SE MUESTRAN LAS GRAFICAS 
web.plotly_chart(fig, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 
web.plotly_chart(fig_derivada, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 


# Analisis en la toma de decisones 
web.subheader("Análisis para la toma de decisiones")
web.write(
    "La organización debe analizar el comportamiento de los ingresos "
    "para identificar el momento de mayor rendimiento de la campaña."
)


# Muestra la interpretacion y recomendacion 

web.info(interpretacion) # Muestra el mensaje segun la tasa de variación 

web.success(recomendacion)