from pickle import load
import streamlit as st

model = load(open('/workspaces/appweb_ml_streamlit/src/random_forest_42.sav','rb'))

st.title('Predicción de Nota en Exámen')

#[['Hours_Studied','Attendance','Previous_Scores','Tutoring_Sessions',
# 'Parental_Involvement_num','Access_to_Resources_num']]

horas_estudio = st.slider('Horas de estudio', min_value=1,max_value=44,step=1)
asistencia = st.slider('Asistencia', min_value=60,max_value=100,step=1)
nota_previa = st.slider('Nota anterior obtenida', min_value=50,max_value=100,step=1)
sesiones_tutoria = st.slider('Sesiones de tutoría', min_value=0,max_value=8,step=1)
involucramiento_padres = st.radio('Involucramiento de los padres',['Bajo','Medio','Alto'],index=None)
acceso_recursos = st.radio('Acceso a recursos',['Bajo','Medio','Alto'],index=None)

#diccionarios para traducir inputs y aplicarlos al modelo
involucramiento_padres_dicc = {'Bajo':0,'Medio':1,'Alto':2}
acceso_recursos_dicc = {'Bajo':2,'Medio':1,'Alto':0}

if st.button('Predecir'):
    prediccion = model.predict([[horas_estudio, asistencia, nota_previa, sesiones_tutoria, involucramiento_padres_dicc[involucramiento_padres], acceso_recursos_dicc[acceso_recursos]]])
    st.write('Nota predecida:', int(prediccion))
