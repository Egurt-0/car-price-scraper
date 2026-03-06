import streamlit as st
from pymongo import MongoClient
from rascunho_backend_projeto import colecao, conexao



st.title("Trivago Automobilistico")
busca = st.text_input("qual carro deseja procurar")
if busca:
    resultado_busca = colecao.find({"nome": {"$regex": busca, "$options": "i"}})
    for carro in resultado_busca:
        st.subheader(carro["nome"])
        st.write(f"Preço: R${carro['precos']}")
        st.write(f"Link: {carro['link']}")