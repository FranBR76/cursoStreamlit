import streamlit as st
import datetime
st.title("Seja bem-vindo novo aluno")

col1, col2 = st.columns(2,  vertical_alignment="top", gap="large")


with col1:
  st.header("Informe seus dados")
  st.text_input("Nome")
  st.text_input("Sobrenome")
 
  today = datetime.datetime.now()
  next_year = today.year + 1
  jan_1 = datetime.date(next_year, 1, 1)
  dec_31 = datetime.date(next_year, 12, 31)

  d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
  )
  d


with col2:
  st.text_input("CEP")
  st.text_input("Endereço")
  st.text_input("Numero")
  st.text_input("Ponto de referencia")
  
