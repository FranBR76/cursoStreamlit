import streamlit as st


def inicio():
  st.header("Bem-vindo(a)!")
  st.subheader("Selecione um exercício da lista 1 através do menu a esquerda.")

#ex 1
def ex1():
  st.subheader("Minha vida vai melhorar agora que estou aprendendo a programar...pelo menos o computador vai entender meus problemas!")


# ex 2
def ex2():
  frase = st.text_input("Digite a frase ''Programar um sistema de confeitaria é igual fazer um bolo: se errar a sintaxe, o código embatuma!'' do exercicio 2: ")
  if frase == "Programar um sistema de confeitaria é igual fazer um bolo: se errar a sintaxe, o código embatuma!":
      st.subheader(f"Frase escrita: {frase}")
  else:
      st.subheader("Frase incorreta, tente novamente.")


#ex 3

  
# receita()

    


def lerIngredientes():  
    st.header("Bolo de Leite Condensado com 3 Ingredientes")
    st.subheader("Ingredientes:")
    st.subheader("1 lata de leite condensado (395g)")
    st.subheader("4 ovos")
    st.subheader("1 xicara de farinha de trigo (120g)")
    
    xicara = st.number_input("Quantas xicaras de farinha de trigo são necessarias para a receita?", step=1)
    gXicara = st.number_input("Quantos gramas que a xicara precisa ter para a receita? ", step=1)
    leiteCondensado = st.number_input("Quantas latas de leite condensado precisa? ", step=1)
    gLeiteCondensado = st.number_input("Quantas gramas tem uma lata de leite condensado de acordo com a receita?", step=1)
    ovos = st.number_input("Quantos ovos precisa? ", step=1)
    if st.button("Verificar"):
      st.subheader("Voce respondeu:")
      st.subheader("Xicaras de farinha de trigo: {}".format(xicara))
      st.subheader("Gramas da xicara: {}".format(gXicara))
      st.subheader(f"Leite condensado: {leiteCondensado}")
      st.subheader(f"Gramas da lata de leite condensado: {gLeiteCondensado}")
      st.subheader(f"Ovos: {ovos}")

# lerIngredientes()




#ex 4
def ex4(): 
    leiteC = st.number_input("Quantos g de leite condensado você usou?")
    leiteC = leiteC * 0.7746835443037975 
    Ovos = st.number_input("Quantos ovos você usou?")
    Ovos = Ovos * 200 
    Farinha = st.number_input("Quantos g de farinha você usou?")
    Farinha = Farinha * 1.1 
    Mltotal = leiteC + Ovos + Farinha 
    print(f"A quantidade total de ml é de: {Mltotal}")
    alturaF = st.number_input("Qual a altura da forma?")
    larguraF = st.number_input("Qual a largura da forma?")
    comprimentoF = st.number_input("Qual o comprimento da forma?") 
    volumeF = alturaF * larguraF * comprimentoF 
    st.write("Interpretando o resultado:") 
    st.write("Para verificar se o tamanho da forma é o suficiente para comportar a receita, devemos comparar a quantidade de ml da receita com o volume. De forma simplificada, podemos dizer que se a quantidade de ml for igual ao valor do volume, o conteúdo da receita caberá na forma. Se a quantidade de ml for maior que o volume, o conteúdo da receita não caberá na forma. Se a quantidade de ml for menor que o volume, o conteúdo cabe na forma.") 
    st.write("Matematicamente: 1cm3 = 1litro = 1ml") 

    

    if Mltotal <= volumeF: 
        st.subheader("O conteúdo da receita caberá na forma.") 
        st.write("Vamos cortar um papel para untar a forma retangular.") 
        # A= b*h - comprimento x largura creio eu 
        papel = larguraF * comprimentoF 
        st.write(f"O papel deve ter {papel} cm2") 
        
        st.write("Para forma redonda:") 
        raio = st.number_input("qual o raio da forma?") 
        altura = st.number_input("qual a altura da forma?") 
        volumeFRedonda = 3.14 * raio**2 * altura 

    if Mltotal <= volumeFRedonda: 
        st.write("O conteúdo da receita caberá na forma.") 
       
        st.write("Vamos cortar um papel para untar a forma redonda.") 
        papelRedondoBase = 3.14 * raio**2 
        papelRedondoLat = 2 * 3.14 * raio * altura 
        papelRedondo = papelRedondoBase + papelRedondoLat 
        st.write(f"O papel deve ter {papelRedondo} de área") 

 
    
# ex 5
 
def ex5():
    st.subheader("Para a versão menos calorica") 
    leiteC = st.number_input("Quantos g de leite condensado você tem?")
    MenosCalorico = leiteC * 0.2 
    MenosCalorico = leiteC - MenosCalorico 
    st.write(f"Use {MenosCalorico} g de leite condensado") 

    

 


# ex 6

def ex6():
    aluguel = st.number_input("Qual seu gasto com aluguel? ")
    energia = st.number_input("Qual seu gasto com energia elétrica? ")
    internet = st.number_input("Qual seu gasto com internet? ")
    agua = st.number_input("Qual seu gasto com água? ")

    if st.button("Ver"):
      fixo = aluguel + energia + internet + agua
      st.write(f"Gasto fixo: {fixo}")
    
  
    leiteC = st.number_input("Qual seu gasto com leite condensado? ")
    ovos =st.number_input("Qual seu gasto com ovos? ")
    farinha = st.number_input("Qual seu gasto com farinha de trigo? ")
    gas = st.number_input("Qual seu gasto com gas? ")
    embalagem = st.number_input("Qual seu gasto com embalagem? ")
    
    variavel = leiteC + ovos + farinha + gas + embalagem
    st.write(f"Gasto variável: {variavel}")
    
    cozinha = st.number_input("Qual seu gasto com o setor da cozinha? ")
    vendas = st.number_input("Qual seu gasto com o setor de vendas? ")
    administrativo = st.number_input("Qual seu gasto com o setor administrativo? ")
    condominio = st.number_input("Qual seu gasto com a anuidade de condomínio? ")
    mei = st.number_input("Qual seu gasto com o MEI? ")
    transporte = st.number_input("Qual o valor do transporte? ")
    embalagem = st.number_input("Qual o valor da embalagem? ")
    
    despesas = cozinha + vendas + administrativo + condominio + mei + transporte + embalagem
    st.write(f"Gasto com despesas: {despesas}")
   
    icms = st.number_input("Qual o valor do ICMS? ")
    frete = st.number_input("Qual o valor gasto com frete? ")
    
    CTA = fixo + variavel + administrativo + icms + frete
    st.write(f"CTA: {CTA}")
    

# CTA()


# ex 7
def markup():
    DV = float(input("Digite o percentual do despesas variáveis: ")) 
    DF = float(input("Digite o percentual do despesas fixas: ")) 
    ML = float(input("Digite o percentual da margem de lucro: ")) 
    M = 100 / (100 - (DV + DF + ML))
    print(f"Markup: {M}%")


# markup()


# ex 8


def encomendas():
    vetor = []
    for i in range(10):
        valor = float(input(f"Digite o valor da encomenda {i+1}: "))
        vetor.append(valor)
    media = sum(vetor) / 10
    print(f"Media das encomendas: {media}")


def main():
  opcao = st.sidebar.selectbox(
    "Escolha um exercicio:",
    ("Inicio", "Exercicio 1", "Exercicio 2", "Exercicio 3", "Exercicio 4", "Exercicio 5")
)
  if opcao == "Inicio":
      inicio()
  elif opcao == "Exercicio 1":
      ex1()
  elif opcao == "Exercicio 2":
      ex2()   
  elif opcao == "Exercicio 3":
      lerIngredientes()   
      
  elif opcao == "Exercicio 4":
      ex4()   
         
  elif opcao == "Exercicio 5":
      ex5()   
         
  elif opcao == "Exercicio 6":
      ex6()   
    

if __name__ == "__main__":
  main()









