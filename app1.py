# 1. Importaciones de las librerias 
        #streamlit: Transforma scripts de python en apliciones web sin necesidad de usar lenguajes webs (HTML, CSS ,JS)
        # Numpy: Sirve para realizar calculos numericos y cientificos a gran escala
        # ploty: Sirve para crear graficos interactivos con sus dashboard
        # Pandas: Sirve para el analisis datos tabulares(filas y columnas)
# python -m streamlit run app1.py
import streamlit as web
import numpy as num
import plotly as plot 

# FIN DE LAS IMPORTACIONES DE LAS LIBRERIAS 


# 2.CONFIGURACION DE LA APLICACION 

web.title("Campaña publicitaria Situación 2B") # Titulo para la pagina 
web.subheader("Situación en Contexto") # Subtitulo 
web.write("**Campaña publicitaria, producción y precio**")

web.write(
    "Los ingresos diarios de la campaña, en miles de pesos, "
    "el día x son:"
)

web.latex(r"""
I(x)=
\begin{cases}
-2x^2+80x+500 & \text{si } x \leq 25\\
1350-15(x-25) & \text{si } x > 25
\end{cases}
""")
web.write("""La campaña fue contratada por 60 días. Para el material
publicitario, la imprenta puede producir como máximo 3.000
unidades. Para el programa de fidelización, el área de
mercadeo estima 𝑞 = 1200 − 30𝑝 suscriptores con un precio
de p miles de pesos, y cada suscriptor le cuesta a la empresa 8
mil pesos.""")
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
web.write("Los ingresos diarios de la campaña, en miles de pesos, el día x son")
# PREGUNTA 1: DOMINIO DE LAS FUNCIONES

with web.expander("Pregunta 1. Dominio de las funciones", expanded=True): # EXPANDIBLE 
    web.markdown("### Enunciado")
    web.write(
        """ Determinen el dominio de I(x), de la producción q y del precio p
            a partir de la información del escenario. ¿Qué condición del
            contexto fija cada extremo del precio?"""
    )
    web.markdown("### Respuesta:")
    # 1. Dominio de los días de campaña

    web.markdown("**A. Dominio de los días de campaña**")
    web.latex(r"0 \leq 60") # Lenguaje iterado para poder vizualizar 

    web.write(
        "La campaña tiene una duración contratada de 60 días. " # Conclusiones 
        "Por tanto, no se consideran días negativos ni días "
        "posteriores a la finalización del contrato."
    )

    # 2. Dominio de la producción

    web.markdown("**B. Dominio de la producción**")

    web.latex(r"0 \leq 3000") # Lenguaje iterado para poder vizualizar 

    web.write(
        "La producción no puede ser negativa y la capacidad " # Conclusiones 
        "máxima de impresión es de 3.000 unidades."
    )
    # 3. Dominio del precio

    web.markdown("**C. Dominio del precio**")

    web.latex(r"0 \leq 40") # Lenguaje iterado para poder vizualizar 
 
    web.write(
        "El precio no puede ser negativo. Además, la demanda " # Conclusiones 
        "q = 1200 - 30p debe ser mayor o igual a cero. "
        "Por esta razón, el precio máximo es de 40 mil pesos."
    )





# PREGUNTA 2 

with web.expander("Pregunta 2. Máximos, tasas de variación y continuidad"): # Pregunta 

    web.markdown("### Enunciado") 

    
    web.write("A. ¿Qué día se alcanza el mayor ingreso diario de la primera fase?")
    web.write("B. ¿A qué ritmo crecían los ingresos el día 10?")
    web.write("C. ¿Los ingresos son continuos al pasar a la segunda fase?")
    web.write("D. ¿Cambia su ritmo?")
    
    web.markdown("### Respuesta:")
    # RESPUESTA A DE LA 2
    web.markdown("**A. El día que se alcanza el mayor ingreso diario en la primera fase**")
    web.write(
        "La organización alcanza su máximo ingreso diario "
        "en el día **20**, con un valor de **1.300** miles de pesos, "
        "equivalentes a **$1.300.000**."
    )


    # RESPUESTA B DE LA 2

    web.markdown("**B. Ritmo de crecimiento del dia 10**")
    web.write(
        "En el día 10, los ingresos diarios están aumentando "
        "a una tasa de **40** mil pesos por cada día adicional "
        "de campaña."
    )


    # RESPUESTA C DE LA 2

    web.markdown("**C. Ingresos continuos en la segunda fase**")
    web.write(
        "El modelo original presenta una discontinuidad de salto "
        "en el cambio de fase. La propuesta corregida permite "
        "eliminar esa discontinuidad al igualar el valor de "
        "la segunda fase con el valor de la primera."
    )

    # RESPUESTA D DE LA 2 
    web.markdown("**D. Cambio de ritmo**")
    web.write(
        """Si se registra un cambio de ritmo, en la primera 
        pase se puede ver que tiene un ritmo de **-25**, y en la segunda 
        fase se puede ver un ritmo de **-15**. Con el ajuste hecho en la función
        sigue dando el mismo resultado de **-15**
        
        
        """
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

    web.write("Los ingresos acumulados de la primera fase son:")


    web.markdown("### Enunciado") 
    
    web.latex(r"""
    I_A(x)=-\frac{2}{3}x^3+40x^2+500x
    """)

    web.write(
        "Encuentren el punto de inflexión de $I_A(x)$, "
        "compárenlo con la pregunta 2 y expliquen qué significa "
        "para el área comercial."
    )
    web.markdown("### Respuesta:")

    # RESPUESTA A DE LA 3
    web.markdown("**A. Punto de inflexión:**")

    web.write(""" 
        El punto de inflexión es en el dia **20**, por tal razon los días anteriores
        se tenia un aumento considerablemente rapido. Después de pasado el dia 20 
        los ingresos diarios comienzan a disminuir, pero siguen sumando el ingreso acomulado,
        por tal razon los ingresos siguen subiendo.
    """)

    web.write(""" 
            Adicionalmente el valor que se optiene en el dia 20 corresponde a
            **$20.666.667 de pesos**. 
        """)


    # SLIDER DE LA PREGUNTA 3 
    web.markdown("### Explorador de ingresos acumulados")

    dia_pregunta3 = web.slider(
        "Selecciona el día de la campaña:",
        min_value=0,
        max_value=25,
        value=15,
        step=1,
        key="dia_pregunta3"
    )

    ingreso_acumulado = (
        -(2/3)*dia_pregunta3**3
        + 40*dia_pregunta3**2
        + 500*dia_pregunta3
    )

    # MUESTRA LOS INGRESOS ACOMULADOS 
    web.metric(
        "Ingresos acumulados",
        f"${ingreso_acumulado * 1000:,.0f}"
    )

    x_acumulado = num.linspace(0, 25, 100)

    y_acumulado = (
        -(2/3)*x_acumulado**3
        + 40*x_acumulado**2
        + 500*x_acumulado
    )

    fig_acumulados = plot.graph_objects.Figure()

    # Curva de ingresos acumulados
    fig_acumulados.add_trace(
        plot.graph_objects.Scatter(
            x=x_acumulado,
            y=y_acumulado,
            mode="lines",
            name="Ingresos acumulados",
            line=dict(color="#00bfa6", width=3)
        )
    )

    # Punto del día seleccionado
    fig_acumulados.add_trace(
        plot.graph_objects.Scatter(
            x=[dia_pregunta3],
            y=[ingreso_acumulado],
            mode="markers",
            name="Día seleccionado",
            marker=dict(color="#FF5722", size=12)
        )
    )

    # Punto de inflexión
    fig_acumulados.add_trace(
        plot.graph_objects.Scatter(
            x=[20],
            y=[62000/3],
            mode="markers",
            name="Punto de inflexión",
            marker=dict(color="#11FF00", size=12)
        )
    )

    fig_acumulados.update_layout(
        title="Ingresos acumulados durante la primera fase",
        height=500,
        xaxis=dict(
            title="Días de campaña",
            dtick=2,
            range=[0, 25],
            minallowed= 0, #minallowed: valor minimo de la visualizacion,
            maxallowed= 25 #  maxllowed: valor maximo de la visualizacion
        ),
        yaxis=dict(
            title="Ingresos acumulados (miles de pesos)",
        )
    )

    web.plotly_chart(
        fig_acumulados,
        use_container_width=True
    )

# PREGUNTA 4: PRODUCCION Y COSTOS

with web.expander("Pregunta 4. Producción, costos y beneficios"):

    web.markdown("### Enunciado")

    web.write("")
    web.write(
            """ Producir q unidades de material cuesta 𝐶(𝑞) = 3000 + 12𝑞 +
            0,02𝑞² miles de pesos, y cada unidad se vende a un aliado a
            40 + k mil pesos.
        """)

    web.write("A. ¿Qué ocurre con el costo por unidad cuando se producen muy pocas unidades, es decir, cuando q se acerca a 0? ¿Por qué?")
    web.write("B. ¿Cuántas unidades conviene producir para obtener lamayor utilidad? ¿Con cuántas unidades es menor el costo por unidad? ¿Por qué no coinciden?")


    
    web.markdown("### Respuesta:")


    # RESPUESTA A DE LA 4
    web.markdown("**A. Acercamiento a 0 unidades**")
    
    web.write(
        """Cuando la producción se aproxima a cero, se mantiene un costo fijo de producción de **$3.000.000** por el hecho que se pueden asumir que son
        gastos fijos empresariales que se tiene se podria intuir como ejemplo (arriendo, salarios y demás gastos empresariales).
        """)

    web.markdown("**B. Mayor utilidad, menor costo por unidad y coincidencia.**")

    web.write(
            """Todo depende del valor que tenga K en este punto, para saber la mayor utilidad.
                En este caso para dar respuesta asumiremos que k es cero **dando como resultado 700 unidades**
            """)

    web.write(
                """El costo promedio es mínimo aproximadamente en **387 unidades**. El costo promedio mínimo es cercano a **27,49 miles
                    de pesos por unidad ($27.490 aproximadamente)**.
 
                """)

    web.write(
                    """
                Maximizar la utilidad busca la mayor diferencia entre ingresos y costos totales; minimizar
el costo promedio busca el menor costo por unidad. Son objetivos diferentes, por eso sus cantidades óptimas son
distintas: **700** y aproximadamente **387 unidades**.

                    """)

    
    web.markdown("**Utilidad Máxima**")
    web.latex(r"U(q)=(40+K)q-(3000+12q+0.02q^2)")
    web.markdown("**Valores de K**")

    #SLIDER PREGUNTA 4a 
    valor_k = web.slider(
        "Selecciona el valor de K:",
        min_value=-40,
        max_value=50,
        value=0,
        step=1,
        key="valor_k"
    )
    q = num.linspace(0,3000,3001)
    p = 40 + valor_k
    c = 3000 + 12*q+ 0.02*q**2
    u= p*q-c
    indice_max = num.argmax(u)
    punto_maximo = u[indice_max]

    m = (3000/q) + 12 + 0.02*q 
    indice_min = num.argmin(m)
    cantidad_minima = num.sqrt(3000 / 0.02)

    

    cantidad_maxima = q[indice_max]
    col1, col2 = web.columns(2)
    with col1:
        web.metric("Valor de K", f"{valor_k}")

    with col2:
        web.metric("Precio de venta por unidad (P)", f"${p}")

    with col1:
            web.metric("Cantidad maxima de la utilidad", f"{cantidad_maxima}")
    
   

    fig_mayor_utilidad = plot.graph_objs.Figure()


    # Curva de ingresos acumulados
    fig_mayor_utilidad.add_trace(
        plot.graph_objects.Scatter(
            x= q,
            y=u,
            mode="lines",
            name="La mayor utilidad obtenida",
            line=dict(color="#00bfa6", width=3)
        )
    )

    # Punto del día seleccionado
    fig_mayor_utilidad.add_trace(
        plot.graph_objects.Scatter(
            x=[cantidad_maxima],
            y=[punto_maximo],
            mode="markers",
            name="Punto máximo de utilidad",
            marker=dict(color="#FF5722", size=12)
        )
    )


    fig_mayor_utilidad.update_layout(
            title="Utilidad máxima",
            height=500,
            xaxis=dict(
                title="Cantidad de unidades producidas y vendidas",
                range=[0, 3500],
                minallowed= 0, #minallowed: valor minimo de la visualizacion,
                maxallowed= 3500 #  maxllowed: valor maximo de la visualizacion
            ),
            yaxis=dict(
                title="Utilidad total (miles de pesos)",
                range=[-80000, 80000],
                minallowed= -80000, #minallowed: valor minimo de la visualizacion,
                maxallowed= 80000 #  maxllowed: valor maximo de la visualizacion
            )
        )

    web.plotly_chart(
            fig_mayor_utilidad,
            use_container_width=True
        )



    # RESPUESTA B DE 4 
    web.markdown("**Costo promedio mínimo**")
    valor_q = web.slider(
            "Selecciona la cantidad de unidades (q)",
            min_value=1,
            max_value=3000,
            value=10,
            step=1,
            key="valor_q"
        )
    costo_seleccionado = (3000 / valor_q) + 12 + 0.02 * valor_q
    cordenada_y = (3000 / cantidad_minima) + 12 + 0.02 * cantidad_minima
    
    web.latex(r"C_u(q)=\frac{3000+12q+0.02q^2}{q}")

    col1, col2 = web.columns(2)
    with col1:
        web.metric("Cantidad de unidades producidas ", f"{valor_q} unidades")
    with col2:
        web.metric("Costo promedio por unidades ", f"${costo_seleccionado:.2f} (m de pesos)")

    web.metric("Cantidad minima de costo unitario", f"{cantidad_minima:.2f} unidades")
    fig_menor_costo = plot.graph_objs.Figure()

    
    # dibujo de la función
    fig_menor_costo.add_trace(
        plot.graph_objects.Scatter(
            x= q,
            y= m,
            mode="lines",
            name="La mayor utilidad obtenida",
            line=dict(color="#00bfa6", width=3)
        )
    )

    # Punto del día seleccionado
    fig_menor_costo.add_trace(
        plot.graph_objects.Scatter(
            x=[valor_q],
            y=[costo_seleccionado],
            mode="markers",
            name="Valor de dado a q",
            marker=dict(color="#FF5722", size=12)
        )
    )


    # Punto de inflexión
    fig_menor_costo.add_trace(
        plot.graph_objects.Scatter(
            x=[cantidad_minima],
            y=[cordenada_y],
            mode="markers",
            name="El menor costo por unidad ",
            marker=dict(color="#11FF00", size=12)
        )
    )



    fig_menor_costo.update_layout(
                title="Costo promedio por unidad según la cantidad producida",
                height=500,
                xaxis=dict(
                    title="Cantidad de unidades producidas (q)",
                    range=[0, 3000],
                    minallowed= 0, #minallowed: valor minimo de la visualizacion,
                    maxallowed= 3000 #  maxllowed: valor maximo de la visualizacion
                ),
                yaxis=dict(
                    title="Costo promedio por unidad (miles de pesos)"
                )
            )

    web.plotly_chart(
                fig_menor_costo ,
                use_container_width=True
            )
    

# PREGUNTA 5: PRECIO OPTIMO Y UTILIDAD

with web.expander("Pregunta 5. Precio óptimo y utilidad"):

    web.markdown("### Enunciado")

    web.write(
        "¿Qué precio de suscripción deja la mayor utilidad?",
    )

    web.write(
            "¿Qué ocurre con la utilidad en los extremos del dominio del precio?"
        )

    web.markdown("### Respuesta:")
    web.markdown("**A. Función de utilidad**")

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

    web.write(
        "El precio que maximiza la utilidad es de "
        "**24 mil pesos por suscriptor**."
    )
    web.write(
        "La utilidad máxima es de **7.680 miles de pesos**, "
        "equivalentes a **$7.680.000**."
    )


    web.markdown("**B. Análisis de los extremos del dominio**")

    web.write(
        "El rango del precio es de 0 a 40 mil pesos, "
        "porque el precio no puede ser negativo y la "
        "demanda no puede ser menor que cero."
    )

    web.markdown("**1. Cuando el precio es cero:**")

    web.latex(r"U(0)=(0-8)(1200-30(0))")


    web.write(
        "Cuando el precio es $0, la empresa obtiene una pérdida de **$9.600.000**"
    )

    web.markdown("**2. Cuando el precio es 40 mil pesos:**")

    web.latex(r"U(40)=(40-8)(1200-30(40))")

    web.write(
            "Cuando el precio es **$40.000, la utilidad es cero debido a que no hay suscriptores**."
        )

    #SLIDER PREGUNTA 5 
    web.markdown("**Explorador del precio**")

    precio_seleccionado = web.slider(
        "Selecciona el precio de suscripción:",
        min_value=0,
        max_value=40,
        value=20,
        step=1,
        key="precio_pregunta5"
    )


    cantidad_suscriptores = (
        1200 - 30*precio_seleccionado
    )

    utilidad_seleccionada = (
        (precio_seleccionado - 8)
        * cantidad_suscriptores
    )

    col1, col2 = web.columns(2)

    col1.metric(
        "Utilidad proyectada",
        f"${utilidad_seleccionada * 1000:,.0f}"
    )

    col2.metric(
        "Suscriptores",
        f"{cantidad_suscriptores:,}"
    )


    # Valores para construir la curva
    precios = num.linspace(0, 40, 100)

    utilidades = (
        (precios - 8)
        * (1200 - 30*precios)
    )

    # Crear la figura
    fig_utilidad = plot.graph_objects.Figure()

    # Curva de utilidad
    fig_utilidad.add_trace(
        plot.graph_objects.Scatter(
            x=precios,
            y=utilidades,
            mode="lines",
            name="Función de utilidad",
            line=dict(color="#00bfa6", width=3)
        )
    )

    # Punto del precio seleccionado
    fig_utilidad.add_trace(
        plot.graph_objects.Scatter(
            x=[precio_seleccionado],
            y=[utilidad_seleccionada],
            mode="markers",
            name="Precio seleccionado",
            marker=dict(color="#FF5722", size=12)
        )
    )

    # Punto de utilidad máxima
    fig_utilidad.add_trace(
        plot.graph_objects.Scatter(
            x=[24],
            y=[7680],
            mode="markers",
            name="Máxima utilidad",
            marker=dict(color="#11FF00", size=12)
        )
    )

    # Configuración de la gráfica
    fig_utilidad.update_layout(
        title="Utilidad según el precio de suscripción",
        height=500,
        xaxis=dict(
            title="Precio (miles de pesos)",
            dtick=2,
            range=[0, 40],
            minallowed=0, #minallowed: valor minimo de la visualizacion,
            maxallowed=40 #  maxllowed: valor maximo de la visualizacion

        ),
        yaxis=dict(
            title="Utilidad (miles de pesos)"
        )
    )

    # Mostrar gráfica
    web.plotly_chart(
        fig_utilidad,
        use_container_width=True
    )



# DECISION PROFESIONAL DE LA ORGANIZACION


web.header("Decisión profesional de la organización")

web.write(
    "A partir de los resultados obtenidos en el análisis, se recomienda implementar las siguientes decisiones para la organización:"
)

web.markdown("### 1. Estrategia para la campaña publicitaria")

web.write(
    """
    Se recomienda concentrar la campaña durante los primeros **20 días**, 
    ya que en ese momento se alcanza el ingreso diario máximo de **$1.300.000 pesos**. 
    Después de ese punto, los ingresos comienzan a disminuir, 
    por lo que prolongar la campaña bajo las mismas condiciones podría reducir su rendimiento.
""")

web.write(
    """ Aunque después del **día 20** los ingresos diarios 
    disminuyen, permanecen positivos durante el periodo 
    analizado. Por ello, se propone cumplir los 60 días 
    contratados y realizar seguimiento al rendimiento 
    de la campaña."""
)

web.markdown("### 2. Precio de venta ")

web.write(
    """ 
        Para el programa de fidelización, se recomienda establecer un precio de **$24.000 Pesos**, 
        debido a que este valor maximiza la utilidad del modelo analizado y permite alcanzar una cantidad estimada de 480 suscriptores.
    """
)

web.markdown("### 3. Nivel de producción")

web.write(
    """ 
        El costo promedio por unidad alcanza su mínimo cuando la producción se aproxima a **387 unidades**. 
        Este resultado permite identificar un nivel de producción eficiente desde la perspectiva de los costos.
    """
)

web.write(
    """ 
        Sin embargo, para maximizar la utilidad de la venta a los aliados, 
        la cantidad de producción debe ajustarse según el valor de K y la capacidad máxima de 3.000 unidades.
    """
)

web.markdown("### Conclusión")

web.write(
    """ 
        La organización debería combinar una campaña publicitaria de **20 días**, una estrategia de fidelización con un precio de **$24.000** Pesos y 
        una planificación de la producción basada en el comportamiento de los costos y la utilidad. 
        Estas decisiones permiten aprovechar los resultados del análisis matemático para mejorar la planificación comercial y financiera.
    """
)