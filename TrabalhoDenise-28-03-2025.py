import datetime
import streamlit as st

def infoUser():
  st.header("Informe seus Dados")
  nome = st.text_input("Informe seu nome ")
  sobrenome = st.text_input("Infome o sobrenome ")
  dt_nasc = st.date_input("Informe sua data de nascimento", format="DD.MM.YYYY)
  estadoCivil = st.selectbox(
    "Informe seu estado civil",
    (Solteiro, Casado, Divorciado, Viúvo),
  )
  sexo = st.selectbox(
    "Informe seu sexo",
    (Masculino, Feminino, Outro),
  #   if Outro:
  #     sexo = st.text_input()
  )

  salario = st.float_input("Informe seu Salário")

  st.write("Dados Informados: ")
