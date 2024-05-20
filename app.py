import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import pdfplumber
import tempfile
from streamlit_star_rating import st_star_rating
import tempfile



st.set_page_config(page_title="Alejandro Paredes", page_icon=":bar_chart:", layout="wide")
hide_st_style = """
<style>
#MainMenu {
  visibility: hidden;
  }
footer {
  visibility: hidden;
  }
header {
  visibility: hidden;
}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

@st.cache_data
@st.cache_resource

def get_data():
  df = pd.read_csv('DataBase League of Legends - BD Limpia.csv')
  return df

df = get_data()

selected = option_menu(None, ["Sobre Mi","Portafolio" ,"Dashboard","Reporte", "Feedback", "Referencias"],
    icons=["person-vcard", "folder-fill", 'pie-chart-fill','clipboard-data-fill', 'chat-square-heart-fill', 'database-fill'],
    menu_icon="cast", default_index=0, orientation="horizontal")

# Referencias
if selected == "Referencias":
  st.markdown('<p class="font">Referencias 📑</p>', unsafe_allow_html=True)

  url_Streaming = "https://www.kaggle.com/datasets/barthetur/league-of-legends-2024-competitive-game-dataset/data"
  st.write(f'''Para este trabajo se utilizó las bases de datos de kagle:
  - [Conjunto de datos de Streaming]( {url_Streaming} )
  ''')
  st.markdown('________________________')

# Portafolio
if selected == "Portafolio":
  st.markdown(""" <style> .font {
  font-size:35px ; font-family: 'Cooper Black'; color: #003399;}
  </style> """,unsafe_allow_html=True)

  st.markdown('<p class="font">Portafolio 🗂️</p>', unsafe_allow_html=True)

  st.markdown('________________________')
  opt = st.radio("Selecciona variable",('Proyectos','Certificaciones/Reconocimientos'))
  if opt == 'Proyectos':
    st.markdown('________________________')

    st.sidebar.markdown('''
      # Secciones
      - [Proyectos Destacados](#proyectos-destacados)
      - [Experiencias](#experiencias)
      - [Otros Proyectos](#otros-proyectos)
        - [Proyect manager](#proyect-manager)
        - [Diseno y Creacion del Expediente Medico](#diseno-y-creacion-del-expediente-medico)
      ''', unsafe_allow_html=True)

    st.header('Proyectos Destacados')
    st.markdown('________________________')

    col1, col2, col3 = st.columns([1, 1,1])


    with col1:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>TecStore Análisis de Datos </p>''', unsafe_allow_html=True)
      st.write('''
      -Limpieza y corrección de datos en la base de  \n
      -Diseño de un Datawarehouse\n
      -Creación de Dashboards en Tableau''')

    with col2:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>LabNL Visualización de Datos </p>''', unsafe_allow_html=True)
      st.write('''
      -Propuesta de valor\n
      -Creación de mapa del agua con distintos filtros en Tableau\n
      -Gráficas con los datos obtenidos\n
      Liga: Proyecto Visualización del agua ''')

    with col3:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>Whirlpool Análisis de Datos </p>''', unsafe_allow_html=True)
      st.write('''
      -Limpieza y corrección de datos\n
      -Análisis de los datos\n
      -Creación de Dashboards en Power BI ''')

    st.markdown('________________________')

    col4, col5, col6 = st.columns([1, 1,1])


    with col4:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>Consultor de Neufeld </p>''', unsafe_allow_html=True)
      st.write('''
      -Propuesta para mejorar su negocio digital \n
      -Costos e ingresos para saber la rentabilidad \n
      -Desarrollo de la arquitectura, diagramas y artefactos AS IS \n
      -Desarrollo de la arquitectura, diagramas y artefactos TO BE \n''')

    with col5:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>Consultor de Whirlpool </p>''', unsafe_allow_html=True)
      st.write('''
      -Desarrollo de la arquitectura, diagramas y artefactos AS IS\n
      -Desarrollo de la arquitectura, diagramas y artefactos TO BE\n
      -Propuesta de valor ''')

    with col6:
      st.markdown('''<p style='font-size: 25px; color: #008000;'>Chubb Gestión del cambio </p>''', unsafe_allow_html=True)
      st.write('''
      -Propuesta de TI\n
      -Propuesta de gestión organizacional \n
      -Desarrollo de la arquitectura, diagramas y artefactos AS IS\n
      -Desarrollo de la arquitectura, diagramas y artefactos TO BE ''')

    st.markdown('________________________')

    st.header('Experiencias')
    st.markdown('________________________')

    imagen1 = Image.open(r'Buenfin.jpg')
    imagen2 = Image.open(r'CISCO.jpg')
    imagen3 = Image.open(r'Chubb.jpg')
    imagen4 = Image.open(r'Linkedin.jpg')
    imagen5 = Image.open(r'NY.jpg')
    imagen6 = Image.open(r'SAP.jpg')
    imagen7 = Image.open(r'SUPSA.jpg')
    imagen8 = Image.open(r'Snowflake.jpg')
    imagen9 = Image.open(r'WHP.JPG')
    imagen10 = Image.open(r'cenmun.jpg')
    imagen11 = Image.open(r'dataton.jpg')
    imagen12 = Image.open(r'hult.jpg')
    imagen13 = Image.open(r'intercampus1.png')
    imagen14 = Image.open(r'intercampus2.jpeg')
    imagen15= Image.open(r'japon.jpg')
    imagen16 = Image.open(r'neorishack.jpg')
    imagen17 = Image.open(r'presentacionWHP.JPG')
    imagen18 = Image.open(r'satelite.jpg')
    imagen19 = Image.open(r'tecgear.jpeg')
    imagen20 = Image.open(r'titulofirma.jpg')

    imagenes = {
        'Participación Buen Fin': imagen1,
        'CISCO': imagen2,
        'Chubb': imagen3,
        'Linkedin': imagen4,
        'Nueva York': imagen5,
        'SAP': imagen6,
        'SUPSA': imagen7,
        'Snowflake': imagen8,
        'Whirlpool': imagen9,
        'CENMUN': imagen10,
        'Datathon': imagen11,
        'HultPrize': imagen12,
        'Intercampus Queretaro': imagen13,
        'Intercampus Estado de México': imagen14,
        'Japon': imagen15,
        'Neoris Hackathon': imagen16,
        'Presentación Avances Whirlpool': imagen17,
        'Satelite': imagen18,
        'Equipo Robótica TecGear': imagen19,
        'Firma de Título': imagen20,
      }

    opciones = list(imagenes.keys())


    def mostrar_imagen(imagen):
        st.image(imagen, use_column_width=True)


    seleccion = st.selectbox('Selecciona una imagen', opciones)
    mostrar_imagen(imagenes[seleccion])
    st.markdown('________________________')



    st.header('Otros Proyectos')
    st.markdown('________________________')

    def show_pdf(x):
        with pdfplumber.open(x) as pdf:
            total_pages = len(pdf.pages)
            page_number = st.slider("Seleccione una página", 1, total_pages, 1,)

            selected_page = pdf.pages[page_number - 1]  # Adjusting index for zero-based indexing
            image = selected_page.to_image()

            # Save the PageImage as a PNG file
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                image.save(temp_file.name)

            # Read the temporary file back in as bytes and pass it to st.image()
            with open(temp_file.name, "rb") as file:
                img_data = file.read()
                st.image(img_data)

    st.subheader("Proyect manager")
    PM= show_pdf("Project manager.pdf")
    st.markdown('________________________')

    st.subheader("Diseno y Creacion del Expediente Medico")
    DCEM= show_pdf("Diseño y Creación del Expediente Médico.pdf")
    st.markdown('________________________')
  if opt == 'Certificaciones/Reconocimientos':
    st.markdown('________________________')

# Sobre Mi
if selected == 'Sobre Mi':

  st.markdown(""" <style> .font {
  font-size:35px ; font-family: 'Cooper Black'; color: #003399;}
  </style> """,unsafe_allow_html=True)
  st.markdown('<p class="font">Sobre mi 👨🏻‍💼💻</p>', unsafe_allow_html=True)
  st.write(f'''Bienvenidos a mi página web, yo soy Alejandro Paredes Balgañon.''')

  col1, col2 = st.columns([2, 1])

  with col1:
    st.write(f'''
    Ingeniero en Transformación Digital de Negocios apasionado por el análisis
    y la visualización de datos, con experiencia en la transformación de datos y
    la creación de dashboards que han optimizado la toma de decisiones y el monitoreo
    de KPIs. Busco constantemente desarrollar nuevas habilidades y conocer sobre nuevas
    tecnologías para mantenerme a la vanguardia del campo. \n

    \nHabilidades:\n
    ▪Pensamiento crítico\n
    ▪Trabajo en equipo\n
    ▪Interpretación de datos\n
    ▪Innovación\n
    ▪Creatividad\n
    ▪Liderazgo\n

    \nHabilidades tecnológicas:\n
    ▪Excel\n
    ▪Google Sheets\n
    ▪SQL\n
    ▪Power BI\n
    ▪Looker Studio\n
    ▪Python\n
    ▪Snowflake\n

    \nMotivación:\n
    \nSoy un profesional altamente motivado y con un gran interés en el análisis de datos
    y su aplicación para la toma de decisiones estratégicas. Me apasiona utilizar mi conocimiento
    y habilidades para ayudar a las empresas a mejorar sus procesos y alcanzar sus objetivos. Estoy
    siempre buscando nuevos retos y oportunidades para aprender y crecer profesionalmente.
    ''')

  with col2:
    st.image(r'Yo.jpg', use_column_width=True)

  st.markdown('________________________')

  st.markdown('<p class="font">Idiomas 🌐</p>', unsafe_allow_html=True)
  st.write(f'''
  -Español (Nativo)\n
  -Inglés (Intermedio B2)\n
  -Japonés (Principiante A2)\n
  ''')

  st.markdown('________________________')

  st.markdown('<p class="font">Educación 🎓</p>', unsafe_allow_html=True)
  st.markdown('''<p style='font-size: 25px;'>Ingeniería en Transformación Digital de Negocios </p>''', unsafe_allow_html=True)
  st.write(f'''Promedio: 95.68 \n
  Tecnológico de Monterrey, Campus Monterrey \n
  Agosto 2020 - Junio 2024''')

  st.markdown('<p class="font">Experiencia 💼</p>', unsafe_allow_html=True)
  st.markdown('''<p style='font-size: 25px;'>Digitalent Whirlpool - Analyst D2C LARN 👨🏻‍💻</p>''', unsafe_allow_html=True)
  st.write(f'''Septiembre 2023 - Actualmente ''')
  st.write(f'''
  ▪Creación de Dashboards en Looker Studio \n
  ▪Tratamiento de datos en Python \n
  ▪Uso de APIs para obtener información de los sistemas transaccionales \n
  ▪Análisis de datos y obtención de insights \n
  ▪Planeación de inversión de presupuestos en Paid media LARN 2024 \n
  ▪Automatizaciones de procesos \n
  ▪Proceso de facturación \n
  ▪Seguimiento de pagos con proveedores''')
  st.markdown('________________________')

  contacto_style = """<style>.contacto-section {
      background-color: black;
      padding: 20px;
      border-radius: 10px;
      color: white;
      }</style>"""

  st.markdown(contacto_style, unsafe_allow_html=True)
  st.markdown('<p class="font">Contactar 🔔</p>', unsafe_allow_html=True)

  st.markdown('''
  <p class="contacto-section">
      ✉️ alejandroparedesbalga@gmail.com <br>
      📱 4774057793 <br>
      🌎 Monterrey, Nuevo León
  </p>
  ''', unsafe_allow_html=True)

# Reporte
if selected == 'Reporte':
  st.markdown(""" <style> .font {
  font-size:35px ; font-family: 'Cooper Black'; color: #003399;}
  </style> """,unsafe_allow_html=True)
  st.markdown('<p class="font">Reporte 📋</p>', unsafe_allow_html=True)

  with st.expander("Raw Data:"):
    st.write(df)

  analysis = st.radio("Selecciona Analisis",('Equipos','Comparar'))
  if analysis == 'Equipos':
    colf1, colf2 = st.columns(2)
    with colf1:
      option1 = st.selectbox(
          "Equipo a Analizar", df["teamname"].unique())
      jugadorequipo = df[df["teamname"] == option1]["playername"].unique()

    with colf2:
      option2 = st.multiselect("Jugadores", options = jugadorequipo, default=list(jugadorequipo))

    filter_df = df[(df["teamname"] == option1) & (df["playername"].isin(option2))]

    total_seconds = filter_df["gamelength"].sum()  # Obtener la duración total en segundos
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    duration_formatted = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"  # Formatear la duración

    gold = float(filter_df["totalgold"].sum())
    cs = float(filter_df["total cs"].sum())
    vision = float(filter_df["visionscore"].sum())
    kda = float(((filter_df["kills"].sum() + filter_df["assists"].sum()) / filter_df["deaths"].sum()).round(2))
    winrate = ((filter_df["result"].sum() / len(filter_df)) * 100).round(2)

    col1, col2, col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.subheader("Total Duración:")
        st.subheader(f"⏱ {duration_formatted}")
    with col2:
        st.subheader("Total Oro:")
        st.subheader(f"💰 {gold}")
    with col3:
        st.subheader("Total Farmeo:")
        st.subheader(f"🎯 {cs}")
    with col4:
        st.subheader("Total Visión:")
        st.subheader(f"🔮 {vision}")
    with col5:
        st.subheader("KDA:")
        st.subheader(f"⚔️ {kda}")
    with col6:
        st.subheader("Win Rate:")
        st.subheader(f"⭐ {winrate}%")

    st.markdown('________________________')
    if len(option2) <1:
      st.write("No hay jugadores seleccionados")
    else:
      df_grouped = filter_df.groupby('side')['result'].sum().reset_index()
      max = df_grouped['result'].max()
      maxresult = df_grouped[df_grouped['result'] == max]['side'].tolist()
  
      figura,descripcion = st.columns(2)

    with figura:
      colores = {'Red': 'red', 'Blue': 'blue'}
      fig1 = px.pie(df_grouped, values='result', names='side', color='side',
                    color_discrete_map=colores,
                    title=f'Lado de la grieta del invocador con la que gana más el equipo {option1}')
      st.write(fig1)

      with descripcion:
        
      with st.expander("Descripción:"):
        st.write(f'''
      En esta gráfica podemos en que lado gana más el equipo. Ya que en teoría,
      la orientación del mapa, la fase de selección de campeones y la distribución
      de los objetivos hacen que jugar desde el lado azul haga mucho más probable la
      victoria. Y en este caso el lado con más tasa de victoria es: **{maxresult}** con **{max}**
      ''')
    st.markdown('________________________')
    oplis= ["result","kills"]
  
    option3 = st.selectbox("Metrica", options = oplis)
    if len(option2) <1:
      st.write("No hay jugadores seleccionados")
    else:
      figura2,descripcion2 = st.columns(2)
      if option3 == "result":
        df_groupedchamp = filter_df.groupby('champion')['result'].sum().reset_index().sort_values(by='result', ascending=False)
        max_win = df_groupedchamp['result'].max()
        champions_with_max_win = df_groupedchamp[df_groupedchamp['result'] == max_win]['champion'].tolist()
        with figura2:
          fig2 = px.bar(df_groupedchamp, x='champion', y='result',
                        color_discrete_sequence=['skyblue'], opacity=0.8,
                        title=f'Victorias por campión para el Equipo {option1}')
          st.write(fig2)
        with descripcion2:
          st.write(f'''
        En esta gráfica de barras podemos ver los campeones que más partidas han ganado.
        Esto podría indicarnos parte del meta (Mejores personajes del parche),
        en este caso vemos que el campeón con más victorias es: **{champions_with_max_win}** con **{max_win}**
        ''')

      if option3 == "kills":
        df_groupedchamp2 = filter_df.groupby('champion')['kills'].sum().reset_index().sort_values(by='kills', ascending=False)
        max_kills = df_groupedchamp2['kills'].max()
        champions_with_max_kills = df_groupedchamp2[df_groupedchamp2['kills'] == max_kills]['champion'].tolist()
        with figura2:
          fig3 = px.bar(df_groupedchamp2, x='champion', y='kills',
                        color_discrete_sequence=['skyblue'], opacity=0.8,
                        title=f'Jugadores abatidos usando el campeón por el Equipo {option1}')
          st.write(fig3)
  
        with descripcion2:
          st.write(f'''
        En esta gráfica de barras podemos ver el campeón que más kills ha realizado.
        Esto podría indicarnos la habilidad que se tiene con el personaje,
        en este caso vemos que el campeón con más kills es: **{champions_with_max_kills}** con **{max_kills}** kills
        ''')

    st.markdown('________________________')

    if len(option2) <1:
      st.write("No hay jugadores seleccionados")
    else:
      figura3,descripcion3= st.columns(2)
      filter_df['KDA'] = (filter_df['kills'].sum() + filter_df['assists'].sum()) / filter_df['deaths'].sum()
      df_groupedkda = filter_df.groupby('playername')['KDA'].sum().reset_index().sort_values(by='KDA', ascending=False)
      max_KDA = df_groupedkda['KDA'].max()
      player_with_max_KDA = df_groupedkda[df_groupedkda['KDA'] == max_KDA]['playername'].tolist()
  
      with figura3:
        grouped_stats = filter_df.groupby('playername').agg({
            'kills': 'sum',
            'assists': 'sum',
            'deaths': 'sum'
        }).reset_index()
  
  
        fig4 = px.line(grouped_stats, x='playername', y=['kills','assists','deaths'],
                       labels={'value': 'Cantidad', 'playername': 'Jugador'},
                       title=f'Mostrar K-D-A de los jugadores del equipo {option1}',
                       markers=True)
        st.write(fig4)

        with descripcion3:
          st.write(f'''
          En esta gráfica de lineas podemos ver tanto las muertes, las asistencias y las bajas por jugador.
          Con esto podemos ver tanto la participación de cada uno, como quien suele morir más.
          ''')
  
    st.markdown('________________________')

    estlist = ['dpm', 'damagetakenperminute', 'damagemitigatedperminute']
  
    # Seleccionar estadísticas
    option4 = st.multiselect("Estadísticas", options=estlist, default=list(estlist))
  
    # Verificar si al menos una opción está seleccionada
    if len(option2) < 1:
        st.warning("Debe seleccionar al menos un jugador.")
    else:
        if len(option4) < 1:
            st.warning("Debe seleccionar al menos una estadística.")
        else:
            # Agrupar y sumar las estadísticas seleccionadas
            grouped_estats = filter_df.groupby('playername')[option4].sum().reset_index()
  
            # Inicializar variables para almacenar los jugadores con el máximo valor en cada métrica
            player_with_max = {}
            max_values = {}
  
            for stat in option4:
                max_value = grouped_estats[stat].max()
                players = grouped_estats[grouped_estats[stat] == max_value]['playername'].tolist()
                player_with_max[stat] = players
                max_values[stat] = max_value

            # Mostrar gráficos y descripciones
            fig, desc = st.columns(2)
            with fig:
                figest = px.bar(grouped_estats, x='playername', y=option4, barmode='group',
                                labels={'playername': 'Jugador', 'value': 'Total', 'variable': 'Estadística'},
                                title=f'Estadísticas para el Equipo {option1}')
                st.write(figest)
            with desc:
                descriptions = []
                for stat in option4:
                    descriptions.append(f"**{stat}**: {', '.join(player_with_max[stat])} con **{max_values[stat]}**")
                
                st.write(f'''
                En esta gráfica de barras podemos ver las estadísticas seleccionadas 
                por cada jugador. Esto es muy importante por el papel que tiene cada campeón y que cumpla con su tarea. 
                Los jugadores destacados en cada métrica son:
                {'<br>'.join(descriptions)}
                ''')

    st.markdown('________________________')
    if len(option2) < 1:
        st.warning("Debe seleccionar al menos un jugador.")
    else:
      cols,dess= st.columns(2)
      
      sun = px.sunburst(
          df,
          path=['side', 'split', 'league', 'teamname'],
          values='result',
          color='side',
          color_discrete_map={'Red': 'red', 'Blue': 'blue'},
          title=f'SunBurst'
      )

      # Renderizar el gráfico de sunburst en Streamlit
      st.plotly_chart(sun,use_container_width = True)
      st.write("Grafica de sunburst para ver las victorias en las siguientes variables")


# Dashboard
if selected == 'Dashboard':
  st.header("Dashboard :bar_chart:")

  analysis = st.radio("Selecciona Analisis",('Equipos','Comparar'))
  
  if analysis == 'Equipos':
    colf1, colf2 = st.columns(2)
    with colf1:
      option1 = st.selectbox(
         "Equipo a Analizar", df["teamname"].unique())
      jugadorequipo = df[df["teamname"] == option1]["playername"].unique()

      with colf2:
        option2 = st.multiselect("Jugadores", options = jugadorequipo, default=list(jugadorequipo))

    filter_df = df[(df["teamname"] == option1) & (df["playername"].isin(option2))]

    total_seconds = filter_df["gamelength"].sum()  # Obtener la duración total en segundos
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    duration_formatted = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"  # Formatear la duración

    gold = float(filter_df["totalgold"].sum())
    cs = float(filter_df["total cs"].sum())
    vision = float(filter_df["visionscore"].sum())
    kda = float(((filter_df["kills"].sum() + filter_df["assists"].sum()) / filter_df["deaths"].sum()).round(2))
    winrate = ((filter_df["result"].sum() / len(filter_df)) * 100).round(2)

    col1, col2, col3,col4,col5,col6 = st.columns(6)
    with col1:
        st.subheader("Total Duración:")
        st.subheader(f"⏱ {duration_formatted}")
    with col2:
        st.subheader("Total Oro:")
        st.subheader(f"💰 {gold}")
    with col3:
        st.subheader("Total Farmeo:")
        st.subheader(f"🎯 {cs}")
    with col4:
        st.subheader("Total Visión:")
        st.subheader(f"🔮 {vision}")
    with col5:
        st.subheader("KDA:")
        st.subheader(f"⚔️ {kda}")
    with col6:
        st.subheader("Win Rate:")
        st.subheader(f"⭐ {winrate}%")

    st.markdown('________________________')

    dash1,dash2 = st.columns(2)
    dash3,dash4= st.columns(2)

    if len(option2) <1:
      st.write("No hay jugadores seleccionados")
    else:
      df_grouped = filter_df.groupby('side')['result'].sum().reset_index()
   
      #grafica 1
      with dash1:
        colores = {'Red': 'red', 'Blue': 'blue'}
        fig1 = px.pie(df_grouped, values='result', names='side', color='side',
                      color_discrete_map=colores,
                      title=f'Lado de la grieta del invocador con la que gana más el equipo {option1}')
        st.write(fig1)
  
      df_groupedchamp = filter_df.groupby('champion')['result'].sum().reset_index().sort_values(by='result', ascending=False)
  
      with dash3:
         grouped_stats = filter_df.groupby('playername').agg({
            'kills': 'sum',
            'assists': 'sum',
            'deaths': 'sum'
            }).reset_index()
         
         fig4 = px.line(grouped_stats, x='playername', y=['kills','assists','deaths'],
                       labels={'value': 'Cantidad', 'playername': 'Jugador'},
                       title=f'Mostrar K-D-A de los jugadores del equipo {option1}',
                       markers=True)
         st.write(fig4)
      
      with dash4:
         estlist = ['dpm', 'damagetakenperminute', 'damagemitigatedperminute']
         # Agrupar y sumar las estadísticas seleccionadas
         grouped_estats = filter_df.groupby('playername')[estlist].sum().reset_index()
         
         figest = px.bar(grouped_estats, x='playername', y=estlist, barmode='group',
                                labels={'playername': 'Jugador', 'value': 'Total', 'variable': 'Estadística'},
                                title=f'Estadísticas para el Equipo {option1}')
         st.write(figest)
      
      sun = px.sunburst(
        df,
        path=['side', 'split', 'league', 'teamname'],
        values='result',
        color='side',
        color_discrete_map={'Red': 'red', 'Blue': 'blue'},
        title=f'SunBurst'
        )
      
      dash2.plotly_chart(sun,use_container_width = True)
      
      fig2 = px.bar(df_groupedchamp, x='champion', y='result',
                  color_discrete_sequence=['skyblue'], opacity=0.8,
                  title=f'Victorias por campión para el Equipo {option1}')
      st.write(fig2)
  

# Feedback
if selected == 'Feedback':
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #003399;}
               </style> """,unsafe_allow_html=True)
    st.markdown('<p class="font">Feedback 📬</p>', unsafe_allow_html=True)


    # Leer el archivo Excel para obtener el último ID de registro
    existing_data = pd.read_excel("forms.xlsx")
    last_id = existing_data['IDR'].max() if not existing_data.empty else 0

    st.markdown('''<p style='font-size: 25px; color: #008000;'>Promedio de calificación </p>''', unsafe_allow_html=True)
   
    average_rating = round(existing_data["Calificación"].mean(), 1)
    if average_rating >= 1:
        star_rating = "⭐" * int(average_rating)
        st.metric("Promedio Calificacion",f"{average_rating} {star_rating}")

        # Crear el formulario en Streamlit
        with st.form(key='Feedback'):  
            nombre = st.text_input("*Nombre:")
            email = st.text_input("*Email:")
            comentario = st.text_area("Comentario:")
            calificacion = st_star_rating("Califica tu experiencia", maxValue=5, defaultValue=3, key="rating")

            # Botón para enviar el formulario
            submit_button = st.form_submit_button(label='Enviar')

        # Verificar si el botón de envío ha sido presionado
        if submit_button:
            # Validar campos obligatorios
            if not nombre:
                st.error("El campo 'Nombre' es obligatorio.")
            elif not calificacion:
                st.error("El campo 'Calificación' es obligatorio.")
            elif not email:
                st.error("El campo de 'Email' es obligatorio")
            else:
                # Incrementar el ID de registro
                last_id = last_id + 1
                
                # Crear un nuevo DataFrame con los datos del formulario actual
                new_data = pd.DataFrame({
                    'IDR': [last_id],
                    'Nombre': [nombre],
                    'Email': [email],
                    'Comentario': [comentario],
                    'Calificación': [calificacion]
                })

                # Concatenar los datos existentes y los nuevos datos
                all_data = pd.concat([existing_data, new_data], ignore_index=True)

                # Guardar todo en el archivo Excel
                all_data.to_excel("forms.xlsx", index=False)
                
                st.write("Gracias por tu feedback!")
                st.write(f"ID de Registro: {last_id}")
                st.write(f"Nombre: {nombre}")
                st.write(f"Email: {email}")
                st.write(f"Comentario: {comentario}")
                st.write(f"Calificación: {calificacion}")
    else:
        star_rating = 0
        st.metric("Promedio Calificacion",f"{average_rating} {star_rating}")

        # Crear el formulario en Streamlit
        with st.form(key='Feedback'):  
            nombre = st.text_input("*Nombre:")
            email = st.text_input("*Email:")
            comentario = st.text_area("Comentario:")
            calificacion = st_star_rating("Califica tu experiencia", maxValue=5, defaultValue=3, key="rating")

            # Botón para enviar el formulario
            submit_button = st.form_submit_button(label='Enviar')

        # Verificar si el botón de envío ha sido presionado
        if submit_button:
            # Validar campos obligatorios
            if not nombre:
                st.error("El campo 'Nombre' es obligatorio.")
            elif not calificacion:
                st.error("El campo 'Calificación' es obligatorio.")
            elif not email:
                st.error("El campo de 'Email' es obligatorio")
            else:
                # Incrementar el ID de registro
                last_id = last_id + 1
                
                # Crear un nuevo DataFrame con los datos del formulario actual
                new_data = pd.DataFrame({
                    'IDR': [last_id],
                    'Nombre': [nombre],
                    'Email': [email],
                    'Comentario': [comentario],
                    'Calificación': [calificacion]
                })

                # Concatenar los datos existentes y los nuevos datos
                all_data = pd.concat([existing_data, new_data], ignore_index=True)

                # Guardar todo en el archivo Excel
                all_data.to_excel("forms.xlsx", index=False)
                
                st.write("Gracias por tu feedback!")
                st.write(f"ID de Registro: {last_id}")
                st.write(f"Nombre: {nombre}")
                st.write(f"Email: {email}")
                st.write(f"Comentario: {comentario}")
                st.write(f"Calificación: {calificacion}")  
