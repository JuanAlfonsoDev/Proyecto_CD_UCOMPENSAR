# 1. Importaciones de las librerias 
        #streamlit: Transforma scripts de python en apliciones web sin necesidad de usar lenguajes webs (HTML, CSS ,JS)
        # Numpy: Sirve para realizar calculos numericos y cientificos a gran escala
        # ploty: Sirve para crear graficos interactivos con sus dashboard
        # Pandas: Sirve para el analisis datos tabulares(filas y columnas)
# python -m streamlit run app.py
import streamlit as web
import numpy as num
import plotly as plot 

# FIN DE LAS IMPORTACIONES DE LAS LIBRERIAS 


# 2.CONFIGURACION DE LA APLICACION 

web.title("Campaña publicitaria Situación 2B") # Titulo para la pagina 
web.subheader("Sistema de análisis de campañas publicitarias") # Subtitulo 
web.write("Panel interactivo para analizar los ingresos y apoyar las decisiones de mercadeo.") # Muestra parrafo en la pantalla 







# FIN DE LAS COSAS VISUALES 


# DATOS PREVIOS A TENER EN CUENTA 
 
x = num.linspace(0, 25, 100) # genera 100 valores de dias entre 0 y 25 
funcion = -2*x**2 + 80*x + 500 #  Es la funcion dada
x2 = num.linspace(25, 60, 100) # Genra 100 valores de dias entre 25 y 60 



# Creacion de la derivada 
derivada = -4*x + 80
# Se crean unos segundo datos para la segunda fase 
x_derivada2 = num.linspace(25, 60, 100) 
derivada2 = num.full_like(x_derivada2, -15) # Se crea un arreglo la mismca cantidad de elementos para poder dibujar 
# FIN DATOS PREVIOS A TENER EN CUENTA  







# DESARROLLO DE LAS PREGUNTAS
web.header("Desarrollo de la actividad")

# PREGUNTA 1: DOMINIO DE LAS FUNCIONES

with web.expander("Pregunta 1. Dominio de las funciones", expanded=True): # EXPANDIBLE 
    web.markdown("### Enunciado")
    web.write(
        "Determinar los dominios de las funciones de ingresos, "
        "producción y precio, justificando sus límites."
    )
    web.markdown("### Respuesta")
    # 1. Dominio de los días de campaña

    web.markdown("**1. Dominio de los días de campaña**")
    web.latex(r"0 \leq x \leq 60") # Lenguaje iterado para poder vizualizar 

    web.write(
        "La campaña tiene una duración contratada de 60 días. " # Conclusiones 
        "Por tanto, no se consideran días negativos ni días "
        "posteriores a la finalización del contrato."
    )

    # 2. Dominio de la producción

    web.markdown("**2. Dominio de la producción**")

    web.latex(r"0 \leq q \leq 3000") # Lenguaje iterado para poder vizualizar 

    web.write(
        "La producción no puede ser negativa y la capacidad " # Conclusiones 
        "máxima de impresión es de 3.000 unidades."
    )
    # 3. Dominio del precio

    web.markdown("**3. Dominio del precio**")

    web.latex(r"0 \leq p \leq 40") # Lenguaje iterado para poder vizualizar 
 
    web.write(
        "El precio no puede ser negativo. Además, la demanda " # Conclusiones 
        "q = 1200 - 30p debe ser mayor o igual a cero. "
        "Por esta razón, el precio máximo es de 40 mil pesos."
    )



# PREGUNTA 2 

with web.expander("Pregunta 2. Máximos, tasas de variación y continuidad"): # Pregunta 

    web.markdown("### Enunciado") 

    web.write(
        "Analizar el comportamiento de los ingresos diarios " # Enunciado 
        "durante la campaña, determinar su máximo en la primera "
        "fase, calcular la tasa de variación en el día 10 "
        "y estudiar la continuidad en el día 25."
    )

    # APARTADO A

    web.markdown("### A. Máximo de ingresos en la primera fase") 

    web.markdown("**Respuesta:** El ingreso máximo se alcanza en el día 20.")

    web.markdown("**Procedimiento matemático:**")

    web.latex(r"I(x)=-2x^2+80x+500") # latex para mostrar funciones matematicas, r permite cadenas de texto facilitando la escritua 

    web.write("Calculamos la primera derivada:")

    web.latex(r"I'(x)=-4x+80")

    web.write("Igualamos la derivada a cero:")

    web.latex(r"-4x+80=0")

    web.latex(r"x=\frac{80}{4}=20")

    web.write("Comprobamos que es un máximo mediante la segunda derivada:")

    web.latex(r"I''(x)=-4<0")

    web.write("Calculamos el ingreso en el día 20:")

    web.latex(r"I(20)=-2(20)^2+80(20)+500")

    web.latex(r"I(20)=1300")

    web.markdown("**Interpretación:**")

    web.write(
        "La organización alcanza su máximo ingreso diario "
        "en el día 20, con un valor de 1.300 miles de pesos, "
        "equivalentes a $1.300.000."
    )


    # APARTADO B

    web.markdown("### B. Tasa de variación en el día 10")

    web.markdown(
        "**Respuesta:** La tasa de variación en el día 10 "
        "es de 40 mil pesos por día."
    )

    web.markdown("**Procedimiento matemático:**")

    web.write("Recordamos la primera derivada:")

    web.latex(r"I'(x)=-4x+80")

    web.write("Evaluamos en el día 10:")

    web.latex(r"I'(10)=-4(10)+80")

    web.latex(r"I'(10)=-40+80=40")

    web.markdown("**Interpretación:**")

    web.write(
        "En el día 10, los ingresos diarios están aumentando "
        "a una tasa de 40 mil pesos por cada día adicional "
        "de campaña."
    )


    # APARTADO C

    web.markdown("### C. Continuidad en el día 25")

    web.write(
        "Se analiza si la función de ingresos es continua "
        "en el punto donde cambia la primera fase a la segunda."
    )

    web.markdown("**1. Valor de la función por la izquierda:**")

    web.latex(r"I(25)=-2(25)^2+80(25)+500")

    web.latex(r"I(25)=1250")

    web.markdown("**2. Límite por la derecha:**")

    web.markdown("**Interpretación:**")

    web.write(
        "El modelo original presenta una discontinuidad de salto "
        "en el cambio de fase. La propuesta corregida permite "
        "eliminar esa discontinuidad al igualar el valor de "
        "la segunda fase con el valor de la primera."
    )

    # SE ESCOGE EL ESCENARIO 
    escenario = web.selectbox(
        "Selecciona el modelo de ingresos:",
        ["Modelo original", "Modelo corregido"],
        key="modelo_pregunta2"
    )

    dia_pregunta2 = web.slider(
        "Selecciona el día de la campaña:",
        min_value=0,
        max_value=60,
        value=10,
        step=1,
        key="dia_pregunta2"
    )

    # SI USA UNA CONDICONAL DEPENDIENDO DEL DIA DE LA CAMAPAÑA 
    if dia_pregunta2 <= 25:
        ingreso_seleccionado = (
            -2*dia_pregunta2**2
            + 80*dia_pregunta2
            + 500
        )
    else:
        if escenario == "Modelo original":
            ingreso_seleccionado = (
                1350 - 15*(dia_pregunta2 - 25)
            )
        else:
            ingreso_seleccionado = (
                1250 - 15*(dia_pregunta2 - 25)
            )

    if dia_pregunta2 < 25:
        tasa_seleccionada = -4*dia_pregunta2 + 80
    elif dia_pregunta2 > 25:
        tasa_seleccionada = -15
    else:
        tasa_seleccionada = None


    if escenario == "Modelo original": # Es la segunda funcion 
        funcion2 = 1350 - 15*(x2 - 25)
    else:
        funcion2 = 1250 - 15*(x2 - 25) 

        
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
            dtick=5, # dictk(muestra los saltos en x en este cado de 2),
            range=[0, 60], # range: el rango de vista(desde,hasta),
            minallowed=0, #minallowed: valor minimo de la visualizacion,
            maxallowed=60 #  maxllowed: valor maximo de la visualizacion
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
        x=[dia_pregunta2],
        y=[ingreso_seleccionado], # indicamos el ingreso segun x de pesos en el eje y 
        mode="markers",  # Muestra un marcador no una linea 
        name="Día seleccionado", # Indica el nombe del marcador
        marker=dict(color="#FF5722", size=12) # Colo del punto maximo
    ))

    fig.add_trace(plot.graph_objects.Scatter(
        x=[20], # Ubicamos el punto del usuario en x
        y=[1300], # indicamos el ingreso segun x de pesos en el eje y 
        mode="markers",  # Muestra un marcador no una linea 
        name="Maximo de ingresos", # Indica el nombe del marcador
        marker=dict(color="#11FF00", size=12) # Colo del punto maximo
    ))
    web.plotly_chart(fig, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 

    # CONSTRUCCION DE LA 2 GRAFICA
    fig_derivada = plot.graph_objects.Figure() # Se crea una nueva figura vacia 


    fig_derivada.add_trace(plot.graph_objects.Scatter(
        x=x, # Valores en x de la grafica 
        y=derivada, # valores en y de la grafica 
        mode="lines", # linea continua 
        name="Tasa de variación", # titulo de la grafica 
        line=dict(color="#00bfa6", width=3) # Color de la linea 
        ))

    fig_derivada.add_trace(plot.graph_objects.Scatter(
        x=x_derivada2,  #Valores en x de la grafica 
        y=derivada2, # valore en y de la grafica 
        mode="lines", # linea continua 
        name="Segunda fase", # titulo de la grafica 
        line=dict(color="#FF9800", width=3) # color de la linea 
    ))


    fig_derivada.update_layout(
        title="Tasa de variación de los ingresos", # titulo de la grafica 
        height=500, # altura de la graica
        width=800, # ancho de la grafica
        xaxis=dict(
            title="Días de campaña", #Titulo de x
            dtick=5, # dictk(muestra los saltos en x en este cado de 1),
            range=[0, 60], # range: el rango de vista(desde,hasta),
            minallowed=0, #minallowed: valor minimo de la visualizacion,
            maxallowed=60 #  maxllowed: valor maximo de la visualizacion
        ),
        yaxis=dict(
            title="Variación (miles de pesos por día)", # titulo del eje y"
            dtick=10, # dictk(muestra los saltos en x en este cado de 1),
            range=[-20, 80], # range: el rango de vista(desde,hasta),
            minallowed= -20, #minallowed: valor minimo de la visualizacion,
            maxallowed= 80 #  maxllowed: valor maximo de la visualizacion
        )  
    )
    if tasa_seleccionada is not None:

        fig_derivada.add_trace(plot.graph_objects.Scatter(
            x=[dia_pregunta2],
            y=[tasa_seleccionada],
            mode="markers",
            name="Día seleccionado",
            marker=dict(color="#FF5722", size=12)
        ))

    else:
        web.warning(
            "En el día 25 la derivada no existe, "
            "porque la función no es derivable en ese punto."
        )

    fig_derivada.add_trace(plot.graph_objects.Scatter( # Punto critico de la derivada
        x=[20],  # Punto cricio en x 
        y=[0], # Punto cricio en y
        mode="markers", # Muestra un marcador no una linea
        name="Punto critico: Dia 20", # Indica el nombe del marcador
        marker=dict(color="#11FF00", size=12) # Color del punto critico
    ))
    # FIN DE LA CONSTRUCCION DE LA 2 GRAFICA
    web.plotly_chart(fig_derivada, use_container_width=True) # Muestra la grafica en la web  y usa todo el ancho y alto disponible 




# FIN CONSTRUCCION DE LA 1 GRAFICA  


# PREGUNTA 3: INGRESOS ACUMULADOS

with web.expander("Pregunta 3. Ingresos acumulados y punto de inflexión"):

    web.markdown("### Enunciado")

    web.write(
        "Analizar la función de ingresos acumulados, "
        "determinar su punto de inflexión e interpretar "
        "su significado comercial."
    )


    web.markdown("### Respuesta")

    web.markdown("**Función de ingresos acumulados:**")

    web.latex(r"I_A(x)=-\frac{2}{3}x^3+40x^2+500x")

    web.write(
        "Esta función representa los ingresos acumulados "
        "durante la primera fase de la campaña, desde el día "
        "0 hasta el día 25."
    )

    web.markdown("### Primera derivada")

    web.write(
        "Derivamos la función de ingresos acumulados:"
    )

    web.latex(
        r"I_A'(x)=-2x^2+80x+500"
    )

    web.write(
        "La primera derivada representa los ingresos diarios "
        "durante la primera fase."
    )


    web.markdown("### Segunda derivada")

    web.write(
        "Derivamos nuevamente para analizar la concavidad "
        "de la función:"
    )

    web.latex(r"I_A''(x)=-4x+80")

    web.markdown("### Cálculo del punto de inflexión")

    web.write(
        "Igualamos la segunda derivada a cero:"
    )

    web.latex(r"-4x+80=0")

    web.latex(r"x=\frac{80}{4}=20")

    web.write(
        "El punto de inflexión ocurre en el día 20."
    )

    web.markdown("### Evaluación de la función")

    web.write(
        "Calculamos los ingresos acumulados en el día 20:"
    )

    web.latex(
        r"I_A(20)=-\frac{2}{3}(20)^3+40(20)^2+500(20)"
    )

    web.latex(r"I_A(20)=\frac{46000}{3}")

    web.latex(r"I_A(20)\approx15333.33")


    web.markdown("### Interpretación comercial")

    web.write(
        "Hasta el día 20, los ingresos diarios aumentan y, "
        "por tanto, los ingresos acumulados crecen cada vez "
        "más rápido."
    )

    web.write(
        "En el día 20 se alcanza el máximo de ingresos diarios. "
        "Después de ese momento, los ingresos diarios comienzan "
        "a disminuir, pero siguen siendo positivos."
    )

    web.write(
        "Por esta razón, los ingresos acumulados continúan "
        "aumentando, aunque a un ritmo cada vez menor."
    )

    web.success(
        "Conclusión: el día 20 representa el punto de inflexión "
        "de los ingresos acumulados y el momento de mayor "
        "generación de ingresos diarios."
    )

# PREGUNTA 4: PRODUCCION Y COSTOS

with web.expander("Pregunta 4. Producción, costos y beneficios"):

    web.markdown("### Enunciado")

    web.write(
        "Analizar el comportamiento de los costos de producción, "
        "determinar la cantidad de unidades que maximiza los "
        "beneficios y encontrar el nivel de producción que "
        "minimiza el costo unitario."
    )

    web.markdown("### Función de costos")

    web.latex(r"C(q)=3000+12q+0.02q^2")

    web.write(
        "La función representa el costo total de producción "
        "en miles de pesos, donde q corresponde a la cantidad "
        "de unidades producidas."
    )



    # APARTADO A: COSTO UNITARIO

    web.markdown("### A. Comportamiento del costo unitario")

    web.write(
        "Para calcular el costo unitario, dividimos el costo "
        "total entre la cantidad de unidades producidas."
    )

    web.latex(
        r"C_u(q)=\frac{C(q)}{q}"
    )

    web.write("Sustituimos la función de costos:")

    web.latex(
        r"C_u(q)=\frac{3000+12q+0.02q^2}{q}"
    )

    web.write("Simplificamos:")

    web.latex(
        r"C_u(q)=\frac{3000}{q}+12+0.02q"
    )

    web.markdown("### Límite cuando la producción se aproxima a cero")

    web.latex(
        r"\lim_{q\to0^+}C_u(q)=+\infty"
    )

    web.write(
        "Cuando la producción se aproxima a cero por valores "
        "positivos, el costo unitario tiende a infinito debido "
        "al costo fijo de producción de 3.000 miles de pesos."
    )

    web.success(
        "Conclusión: producir muy pocas unidades genera un "
        "costo unitario muy elevado, porque el costo fijo "
        "se distribuye entre una cantidad pequeña de unidades."
    )

# PREGUNTA 5: PRECIO OPTIMO Y UTILIDAD

with web.expander("Pregunta 5. Precio óptimo y utilidad"):

    web.markdown("### Enunciado")

    web.write(
        "Determinar el precio que maximiza la utilidad del "
        "programa de fidelización y analizar qué sucede con "
        "la utilidad en los extremos del dominio del precio."
    )

    web.markdown("### Función de utilidad")

    web.write(
        "La utilidad se calcula multiplicando la ganancia "
        "por suscriptor por la cantidad de suscriptores."
    )

    web.latex(
        r"U(p)=(p-8)(1200-30p)"
    )

    web.write(
        "Donde p representa el precio de la suscripción "
        "en miles de pesos y 1200 - 30p representa "
        "la cantidad de suscriptores."
    )


    web.markdown("### Primera derivada")

    web.write(
        "Primero desarrollamos la función de utilidad:"
    )

    web.latex(
        r"U(p)=(p-8)(1200-30p)"
    )

    web.latex(
        r"U(p)=-30p^2+1440p-9600"
    )

    web.write(
        "Derivamos la función respecto al precio:"
    )

    web.latex(
        r"U'(p)=-60p+1440"
    )

    web.markdown("### Encontrar el precio óptimo")

    web.write(
        "Igualamos la primera derivada a cero para encontrar "
        "el punto crítico:"
    )

    web.latex(
        r"-60p+1440=0"
    )

    web.latex(
        r"p=\frac{1440}{60}=24"
    )

    web.success(
        "El precio que maximiza la utilidad es de "
        "24 mil pesos por suscriptor."
    )


    web.markdown("### Segunda derivada")

    web.write(
        "Calculamos la segunda derivada para comprobar "
        "si el punto crítico corresponde a un máximo."
    )

    web.latex(r"U''(p)=-60")

    web.write(
        "Como la segunda derivada es negativa, la función "
        "presenta un máximo."
    )

    web.markdown("### Cálculo de la utilidad máxima")

    web.write(
        "Evaluamos el precio óptimo en la función de utilidad:"
    )

    web.latex(
        r"U(24)=(24-8)(1200-30(24))"
    )

    web.latex(
        r"U(24)=16(480)"
    )

    web.latex(
        r"U(24)=7680"
    )

    web.success(
        "La utilidad máxima es de 7.680 miles de pesos, "
        "equivalentes a $7.680.000."
    )

    web.write(
        "A este precio se obtiene una cantidad de "
        "480 suscriptores."
    )

    web.markdown("### Análisis de los extremos del dominio")

    web.write(
        "El dominio del precio es de 0 a 40 mil pesos, "
        "porque el precio no puede ser negativo y la "
        "demanda no puede ser menor que cero."
    )

    web.markdown("**1. Cuando el precio es cero:**")

    web.latex(r"U(0)=(0-8)(1200-30(0))")

    web.latex(r"U(0)=(-8)(1200)=-9600")

    web.write(
        "La utilidad es negativa en 9.600 miles de pesos, "
        "porque no se cobra la suscripción, pero se incurre "
        "en el costo de atender a los suscriptores."
    )

    web.markdown("**2. Cuando el precio es 40 mil pesos:**")

    web.latex(r"U(40)=(40-8)(1200-30(40))")

    web.latex(r"U(40)=(32)(0)=0")

    web.write(
        "La utilidad es cero porque a ese precio la demanda "
        "desaparece y no hay suscriptores."
    )

    web.markdown("### Interpretación comercial")

    web.success(
        "La organización debe establecer un precio de "
        "$24.000 por suscripción para alcanzar una utilidad "
        "máxima de $7.680.000, con 480 suscriptores."
    )



# ==========================================
# DECISION PROFESIONAL DE LA ORGANIZACION
# ==========================================

web.header("Decisión profesional de la organización")

web.write(
    "A partir de los resultados matemáticos obtenidos, "
    "la organización debe establecer estrategias que "
    "permitan aprovechar los ingresos de la campaña, "
    "optimizar el programa de fidelización y controlar "
    "los costos de producción."
)

web.markdown("### 1. Estrategia para la campaña publicitaria")

web.write(
    "Se recomienda aprovechar el día 20 como el momento "
    "de mayor generación de ingresos diarios, ya que "
    "se alcanza un valor de 1.300 miles de pesos."
)

web.write(
    "Aunque después del día 20 los ingresos diarios "
    "disminuyen, permanecen positivos durante el periodo "
    "analizado. Por ello, se propone cumplir los 60 días "
    "contratados y realizar seguimiento al rendimiento "
    "de la campaña."
)

web.markdown("### 2. Modelo de ingresos")

web.write(
    "Se propone utilizar el modelo corregido como "
    "alternativa de mejora, porque permite garantizar "
    "la continuidad de los ingresos en el día 25. "
    "Esta modificación debe ser validada por la "
    "organización antes de su implementación."
)

web.markdown("### 3. Estrategia de fidelización")

web.write(
    "Se recomienda establecer un precio de suscripción "
    "de $24.000 por persona, debido a que este valor "
    "maximiza la utilidad del programa."
)

web.write(
    "Con este precio se proyectan 480 suscriptores "
    "y una utilidad máxima de $7.680.000."
)

web.markdown("### 4. Producción y control de costos")

web.write(
    "La organización debe respetar la capacidad máxima "
    "de impresión de 3.000 unidades y analizar los costos "
    "antes de establecer el volumen definitivo de producción."
)

web.warning(
    "La cantidad óptima de producción queda pendiente "
    "hasta conocer el valor de k y completar el análisis "
    "de costos y beneficios."
)

web.markdown("### Conclusión general")

web.success(
    "La organización debe aprovechar el máximo rendimiento "
    "de la campaña, establecer un precio de suscripción "
    "competitivo de $24.000 y controlar sus costos de "
    "producción. Las decisiones definitivas deberán "
    "respaldarse con los resultados del análisis económico."
)
