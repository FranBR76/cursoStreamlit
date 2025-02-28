import streamlit as st
st.title("Seja bem-vindo novo aluno")

col1, col2 = st.columns(2)


with col1:
  st.header("Informe seus dados")
  title = st.text_input("Nome")
