import streamlit as st

col1, col2 = st.columns(2)
st.header("Seja bem-vindo novo aluno")
with col1:
  st.title("Informe seus dados")
  title = st.text_input("Nome")
