import streamlit as st
import datetime
st.title("Seja bem-vindo novo aluno")
st.header("Informe seus dados")
col1, col2 = st.columns(2,  vertical_alignment="top", gap="large")
col1, col2 = st.columns([5, 2])

with col1:
  
  st.text_input("Nome")
  st.text_input("Sobrenome")
  st.text_input("CPF")
  
 
  today = datetime.datetime.now()
  next_year = today.year + 1
  jan_1 = datetime.date(next_year, 1, 1)
  dec_31 = datetime.date(next_year, 12, 31)

  st.date_input(
    "Data de nascimento",
    
    format="DD.MM.YYYY",
  )
  


with col2:
  st.text_input(
    "CEP",
    
  )
  
  st.text_input("Endereço")
  st.text_input("Numero")
  st.text_input("Ponto de referencia")
  
