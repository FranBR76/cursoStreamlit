
import streamlit as st

def exercicio_1():
    st.subheader("Exercício 1: Calculadora de IMC")
    peso = st.number_input("Peso (kg):", min_value=1.0, step=0.1)
    altura = st.number_input("Altura (m):", min_value=0.5, step=0.01)
    if st.button("Calcular IMC"):
        calcular_imc(peso, altura)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    st.success(f"Seu IMC é: {imc:.2f}")

def exercicio_2():
    st.subheader("Exercício 2: Conversor de Temperatura")
    celsius = st.number_input("Temperatura em Celsius:", step=0.1)
    if st.button("Converter para Fahrenheit"):
        converter_temperatura(celsius)

def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

def exercicio_3():
    st.subheader("Exercício 3: Contador de Palavras")
    texto = st.text_area("Digite seu texto:")
    if st.button("Contar Palavras"):
        contar_palavras(texto)

def contar_palavras(texto):
    palavras = len(texto.split())
    st.success(f"O texto contém {palavras} palavras.")

def main():
    # Adicionando o selectbox na sidebar
    opcao = st.sidebar.selectbox(
        "Escolha um exercício:",
        ("Calculadora de IMC", "Conversor de Temperatura", "Contador de Palavras")
    )

    if opcao == "Calculadora de IMC":
        exercicio_1()
    elif opcao == "Conversor de Temperatura":
        exercicio_2()
    elif opcao == "Contador de Palavras":
        exercicio_3()

if __name__ == "__main__":
    main()
