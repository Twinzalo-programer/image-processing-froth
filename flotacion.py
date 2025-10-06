import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d

unsafe_allow_html=True


st.write("""
FLOTACIÓN
""")
st.subheader("<h1>lala</h1>")

st.sidebar.header('Performance en la flotación')


def user_input_features():
    largo = st.sidebar.slider('largo', 4.3, 7.9, 5.4)
    alto = st.sidebar.slider('alto', 2.0, 4.4, 3.4)
    x = st.sidebar.slider('x', 1.0, 6.9, 1.3)
    y = st.sidebar.slider('y', 0.1, 2.5, 0.2)
    data = {'largo': largo,
            'alto': alto,
            'x': x,
            'y': y}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.subheader('Parámetros de entrada')
st.write(df)

st.subheader('Datos de flotación')
dff= pd.read_csv('Reporte Flotacion.csv')
st.write(dff)
dff.head(3)

dff2= pd.read_csv('Reporte Flotacion - flujos.csv')
st.write(dff2)

st.write(dff["P80 (micras)"].describe())#[4]



P80_Finos=dff["P80 (micras)"].describe()[4]
P80_Medio=dff["P80 (micras)"].describe()[5]
P80_Gruesos=dff["P80 (micras)"].describe()[6]

def CAT_P80(c):
  if c['P80 (micras)'] >= P80_Gruesos:
    return 'Grueso'
  elif c['P80 (micras)'] <= P80_Finos:
    return 'Fino'
   
  else:
    return 'Medio'

dff['CAT_P80']=dff.apply(CAT_P80, axis=1)


set1=dff["P80 (micras)"].values
hist_data=sns.distplot(set1).get_lines()[0].get_data()
ipf1 = interp1d(x=hist_data[0], y=hist_data[1])
plt.plot([P80_Finos, P80_Finos], [0, ipf1(P80_Finos)], label = "Finos")
plt.plot([P80_Medio, P80_Medio], [0, ipf1(P80_Medio)], label = "Medio")   
plt.plot([P80_Gruesos, P80_Gruesos], [0, ipf1(P80_Gruesos)], label = "Gruesos")   

st.pyplot(plt)



