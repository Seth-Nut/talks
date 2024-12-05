import streamlit as st
import pandas as pd

st.title("¡Bienvenidos a Streamlit!")
st.header("Subtítulo")
st.text("Texto simple para explicar algo.")

if st.button("¡Haz clic aquí!"):
    st.write("¡Botón presionado!")

opcion = st.selectbox("Elige una opción:", ["Opción 1", "Opción 2", "Opción 3"])
st.write(f"Elegiste: {opcion}")

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"Hola, {nombre}!")

data = {"Nombre": ["Ana", "Luis", "Pedro"], "Edad": [23, 30, 35]}
df = pd.DataFrame(data)
st.write("Aquí hay un DataFrame:")
st.dataframe(df)

if st.checkbox("¿Mostrar mensaje secreto?"):
    st.write("🎉 Eres bastante curios@ 🎉")

color = st.radio("Elige un color:", ["Rojo", "Verde", "Azul"])
st.write(f"Color seleccionado: {color}")

col1, col2 = st.columns(2)
with col1:
    st.button("Botón Columna 1")
with col2:
    st.button("Botón Columna 2")

