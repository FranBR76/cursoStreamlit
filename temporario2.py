import streamlit as st
import datetime
st.title("Seja bem-vindo novo aluno")

col1, col2, col3 = st.columns(2,  vertical_alignment="top", gap="large")


with col1:
  st.header("Informe seus dados")
  st.text_input("Nome")
  st.text_input("Sobrenome")
  # numero = st.text_input("CPF")
  # numero =   
  st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
    )


with col2:
  st.text_input("CEP")
  st.text_input("Endereço")
  st.text_input("Numero")
  st.text_input("Ponto de referencia")
  
