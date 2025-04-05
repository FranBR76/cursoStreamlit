import streamlit as st


selEx = st.selectbox("Qual exercicio deseja ver?", "Exercicio 1", "Exercicio 2", "Exercicio 3", "Exercicio 4", "Exercicio 5", "Exercicio 6", "Exercicio 7", "Exercicio 8", "Exercicio 9", "Exercicio 10") 


def ex1():
    ativos = []

    for i in range(10):
        valor = float(input(f"Digite o valor do ativo {i+1}: "))
        ativos.append(valor)

    print("\n\n\n\n")
    print("Ativos:")
    for i in range(10):
        print(f"Ativo {i+1}: {ativos[i]}")



def ex2():
    ex1()

def ex3():
    ativos3 = []

    for i in range(10):
        valor = float(input(f"Digite o valor do ativo {i+1}: "))
        ativos3.append(valor)

    for i in ativos3:
        if i >= 0:
            print(f"Ativo {i}  - (natureza devedora) - valor positivo debita)")
        else:
            print(f"Ativo {i}  - (natureza devedora) - valor negativo credita")


def ex4():
    ativo = []
   

    for i in range(10):
        mes = float(input(f"Digite o valor do ativo {i+1}: "))
        ativo.append(mes)
    
    print("\n\n")

    for i in range(10):
        print(f"Ativo no mês {i+1}: {ativo[i]}")


def ex5():
    obrigacoes = []
    MaiorC = 0
    MenorC = 0

    for i in range(10):
        Ob = float(input(f"Digite o valor da obrigação {i+1}: "))
        obrigacoes.append(Ob)

    caixa = float(input("Digite um valor do caixa"))
    for j in range(10):
        if obrigacoes[j] > caixa:
            MaiorC = MaiorC + 1
        
        else:
            MenorC = MenorC + 1


    print(f"Obrigacoes maiores que o caixa: {MaiorC}")
    print(f"Obrigacoes menores que o caixa: {MenorC}")


def ex6():
    listA = []
    listB = []
    listaTudo = []

    for i in range(10):
        valorA = float(input(f"Digite o valor do ativo {i+1}: "))
        listA.append(valorA)

    for i in range(10):
        valorB = float(input(f"Digite o valor do ativo {i+1}: "))
        listB.append(valorB)

    for i in range(10):
            listaTudo.append(listA[i])
            listaTudo.append(listB[i])
        
    
    for i in range(20):
        print(f"Ativo {i+1}: {listaTudo[i]}")  


def ex7():
    listaA = []
    listaB = []
    listaC = []
    listaD = []

    for i in range(4):
        valorA = float(input(f"Digite o valor {i+1}: Lista A "))
        listaA.append(valorA)
        valorB = input(f"Digite o operador {i+1}: Lista B ")
        listaB.append(valorB)
        valorC = float(input(f"Digite o valor {i+1}: Lista C "))
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

    
    print("\n\n")
   
    print(f"A = | {listaA[0]} | {listaA[1]} | {listaA[2]} | {listaA[3]} |")
    print(f"B = | {listaB[0]} | {listaB[1]} | {listaB[2]} | {listaB[3]} |")
    print(f"C = | {listaC[0]} | {listaC[1]} | {listaC[2]} | {listaC[3]} |")
    print(f"D = | {listaD[0]} | {listaD[1]} | {listaD[2]} | {listaD[3]} |")


def ex8():
    despesas = []

    for i in range(5):
        valorDespesas =float(input("Digite o valor da despesa: "))
        despesas.append(valorDespesas)
    temp = 0
    for i in range(5):
        for i in range(4):
            if despesas[i] < despesas[i+1]:
                temp = despesas[i]
                despesas[i] = despesas[i+1]
                despesas[i+1] = temp

    print(f"Ordem decrescente: {despesas}")


def ex9():
    despesas = []

    for i in range(5):
        valorDespesas =float(input("Digite o valor da despesa: "))
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

    print(f"Ordem decrescente dos valores com multa: {despesas}")
    

def ex10():
    caixa = float(input("Digite o valor do caixa: "))
    
    despesas = []

    for i in range(5):
        valorDespesas =float(input("Digite o valor da despesa: "))
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

    print(f"Ordem decrescente dos valores com multa: {despesas}")

    despesasSomadas = sum(despesas)
    if despesasSomadas > caixa:
        print("Caixa insuficiente para cobrir as despesas")
    else:
        print("Caixa suficiente para cobrir as despesas")
        print(f"Valor restante no caixa: {caixa - despesasSomadas}")
