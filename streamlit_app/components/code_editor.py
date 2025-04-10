import streamlit as st

def editor_codigo():
    codigo = st.text_area("💻 Escreva seu código aqui:", height=300)
    return codigo

