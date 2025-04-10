import streamlit as st
from services.supabase_service import buscar_topicos
from services.openai_service import gerar_desafio, corrigir_codigo
from components.code_editor import editor_codigo

st.set_page_config(page_title="Desafios Python", layout="wide",page_icon="📚")
st.title("💡 Gerador de Desafios em Python com IA")

if st.button("🎯 Me Desafie"):
    topicos = buscar_topicos()
    if topicos:
        enunciado = gerar_desafio(topicos)
        st.write(enunciado)
        st.session_state["enunciado"] = enunciado
    else:
        st.warning("Nenhum tópico encontrado na ementa")

if "enunciado" in st.session_state:
    st.subheader("🧪 Desafio")
    st.write(st.session_state["enunciado"])
    codigo_usuario = editor_codigo()

    if st.button("✅ Corrigir"):
        feedback = corrigir_codigo(st.session_state["enunciado"], codigo_usuario)
        st.subheader("🔍 Feedback da IA:")
        st.write(feedback)



    




