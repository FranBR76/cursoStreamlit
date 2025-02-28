import streamlit as st
st.title("Seja bem-vindo novo aluno")

col1, col2 = st.columns(2,  vertical_alignment="bottom")


with col1:
  st.header("Informe seus dados")
  st.text_input("Nome")
  st.text_input("Sobrenome")
  st.text_input("")


with col2:
  st.text_input("CEP")
  st.text_input("Endereço")
  st.text_input("Numero")
  st.text_input("Ponto de referencia")
  
