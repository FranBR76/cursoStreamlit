import streamlit as st


selEx = st.selectbox("Qual exercicio deseja ver?", ("Exercicio 1", "Exercicio 2", "Exercicio 3", "Exercicio 4", "Exercicio 5", "Exercicio 6", "Exercicio 7", "Exercicio 8", "Exercicio 9", "Exercicio 10")) 



def ex1():
    ativos = []

    for i in range(10):
        valor = st.number_input(f"Digite o valor do ativo {i+1}: ")
        ativos.append(valor)

    
    st.write("Ativos: " "\n")
    for i in range(10):
        st.write(f"Ativo {i+1}: {ativos[i]}")

if selEx == "Exercicio 1" || "Exercicio 2":
    ex1()

def ex3():
    ativos3 = []

    for i in range(10):
        valor = st.number_input(f"Digite o valor do ativo {i+1}: ")
        ativos3.append(valor)

    for i in ativos3:
        if i >= 0:
            st.write(f"Ativo {i}  - (natureza devedora) - valor positivo debita)")
        else:
            st.write(f"Ativo {i}  - (natureza devedora) - valor negativo credita")
            
if selEx == "Exercicio 3":
    ex3()

def ex4():
    ativo = []
   

    for i in range(10):
        mes = st.number_input(f"Digite o valor do ativo {i+1}: ")
        ativo.append(mes)
    
    st.write("\n\n")

    for i in range(10):
        st.write(f"Ativo no mês {i+1}: {ativo[i]}")
if selEx == "Exercicio 4":
    ex4()

def ex5():
    obrigacoes = []
    MaiorC = 0
    MenorC = 0

    for i in range(10):
        Ob = st.number_input(f"Digite o valor da obrigação {i+1}: ")
        obrigacoes.append(Ob)

    caixa = st.number_input("Digite um valor do caixa")
    for j in range(10):
        if obrigacoes[j] > caixa:
            MaiorC = MaiorC + 1
        
        else:
            MenorC = MenorC + 1


    st.write(f"Obrigacoes maiores que o caixa: {MaiorC}")
    st.write(f"Obrigacoes menores que o caixa: {MenorC}")

if selEx == "Exercicio 5":
    ex5()

def ex6():
    listA = []
    listB = []
    listaTudo = []

    for i in range(10):
        valorA = st.number_input(f"Digite o valor do ativo {i+1}: ")
        listA.append(valorA)

    for i in range(10):
        valorB = st.number_input(f"Digite o valor do ativo {i+1}: ")
        listB.append(valorB)

    for i in range(10):
            listaTudo.append(listA[i])
            listaTudo.append(listB[i])
        
    
    for i in range(20):
        st.write(f"Ativo {i+1}: {listaTudo[i]}")  


if selEx == "Exercicio 6":
    ex6()

def ex7():
    listaA = []
    listaB = []
    listaC = []
    listaD = []

    for i in range(4):
        valorA = st.number_input(f"Digite o valor {i+1}: Lista A ")
        listaA.append(valorA)
        valorB = st.text_input(f"Digite o operador {i+1}: Lista B ")
        listaB.append(valorB)
        valorC = st.number_input(f"Digite o valor {i+1}: Lista C ")
        listaC.append(valorC)

    for i in range(4):
        if listaB[i] == "+":
            listaD.append(listaA[i] + listaC[i])
        elif listaB[i] == "-":
            listaD.append(listaA[i] - listaC[i])
        elif listaB[i] == "*":
            listaD.append(listaA[i] * listaC[i])
        elif listaB[i] == "/":
            listaD.append(listaA[i] / listaC[i])

    
    st.write("\n\n")
   
    st.write(f"A = | {listaA[0]} | {listaA[1]} | {listaA[2]} | {listaA[3]} |")
    st.write(f"B = | {listaB[0]} | {listaB[1]} | {listaB[2]} | {listaB[3]} |")
    st.write(f"C = | {listaC[0]} | {listaC[1]} | {listaC[2]} | {listaC[3]} |")
    st.write(f"D = | {listaD[0]} | {listaD[1]} | {listaD[2]} | {listaD[3]} |")
if selEx == "Exercicio 7":
    ex7()

def ex8():
    despesas = []

    for i in range(5):
        valorDespesas =st.number_input("Digite o valor da despesa: ")
        despesas.append(valorDespesas)
    temp = 0
    for i in range(5):
        for i in range(4):
            if despesas[i] < despesas[i+1]:
                temp = despesas[i]
                despesas[i] = despesas[i+1]
                despesas[i+1] = temp

   st.write(f"Ordem decrescente: {despesas}")

if selEx == "Exercicio 8":
    ex8()
def ex9():
    despesas = []

    for i in range(5):
        valorDespesas = st.number_input("Digite o valor da despesa: ")
        despesas.append(valorDespesas)
    temp = 0
    for i in range(5):
        for i in range(4):
            if despesas[i] < despesas[i+1]:
                temp = despesas[i]
                despesas[i] = despesas[i+1]
                despesas[i+1] = temp

    for i in range(5):
        despesas[i] += despesas[i] * 0.1

    st.write(f"Ordem decrescente dos valores com multa: {despesas}")
    
if selEx == "Exercicio 9":
    ex9()
    
def ex10():
    caixa = st.number_input("Digite o valor do caixa: ")
    
    despesas = []

    for i in range(5):
        valorDespesas =st.number_input("Digite o valor da despesa: ")
        despesas.append(valorDespesas)
    temp = 0
    for i in range(5):
        for i in range(4):
            if despesas[i] < despesas[i+1]:
                temp = despesas[i]
                despesas[i] = despesas[i+1]
                despesas[i+1] = temp

    for i in range(5):
        despesas[i] += despesas[i] * 0.1

    st.write(f"Ordem decrescente dos valores com multa: {despesas}")

    despesasSomadas = sum(despesas)
    if despesasSomadas > caixa:
        st.write("Caixa insuficiente para cobrir as despesas")
    else:
        st.write("Caixa suficiente para cobrir as despesas")
        st.write(f"Valor restante no caixa: {caixa - despesasSomadas}")

if selEx == "Exercicio 10":
    ex10()
