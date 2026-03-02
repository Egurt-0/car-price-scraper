import streamlit as st
import pymongo

st.set_page_config(layout='wide')
st.write("""
# Trivago Automobilistico
Aqui voce pode encotrar o carro dos seus sonhos pelo melhor preco
""")
carro = st.text_input("Carro:")