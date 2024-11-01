 class vendedor ():
     def __init__(self, nome):
      self.nome= nome 
        
 vendedor1= vendedor(input('Nome do vendedor:'))
 print('Vendedor: ',vendedor1.nome)        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class pessoa():
  def __init__(self,nome, sobrenome,idade, cidade):
     self.nome = nome
     self.sobrenome= sobrenome
     self.idade= idade
     self.cidade= cidade
     
nome_inp = input('Qual o seu nome? ')
sobrenome_inp=input("Qual o seu sobrenome? ")
idade_inp = int(input("Qual a sua idade? "))
cidade_inp= input('Qual sua cidade? ')

pessoa= pessoa(nome_inp, sobrenome_inp, idade_inp, cidade_inp)
print(f"\nome:{pessoa.nome}\nsobrenome: {pessoa.sobrenome}\nidade: {pessoa.idade}\ncidade:{pessoa.cidade}")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#EX1 resolvido de outra maneira
 class vendedor():
   def __init__(self,nome, nome2):
      self.nome=nome
      self.nome = nome2
         
 def informaCAOSAIDA(self):
     print(f"Olá, meu nome é", self.nome, "e eu tenho")

 vendedor1= vendedor(input('Nome 1'),input('Sobrenome 2'))
 vendedor2= vendedor(input('Nome 2'),None)

 vendedor1.informacaoSaida()
 vendedor2.informacaoSaida()
     
# ex2/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 #26/10/2024

class carro ():
  def _init__(self,marca,ano,cor):
      self.marca = marca
      self.ano = ano
      self.cor = cor

marca_inp=input("Qual a marca do carro")
ano_inp =input("Qual o ano do carro")
cor_inp=input("Qual a cor do carro")

carro= carro(marca_inp,ano_inp,cor_inp)
print(f"\nmarca/:{carro.marca}\nano:{carro.ano}\ncor:{carro.cor}")

#exercicio3 poo////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class pessoa ():
    def _init_(self,cor_de_cabelo, idade, altura, nacionalidade):
        self.cor_de_cabelo = cor_de_cabelo
        self.idade = idade
        self.altura = altura
        self.nacionalidade= nacionalidade
        
cor_de_cabelo_inp = input("Qual a cor do seu cabelo")
idade_inp= input("Qual a sua idade")
altura_inp= input("Qual a sua altura")
nacionalidade_inp= input("Qual a sua nacionalidade")

pessoa= pessoa(cor_de_cabelo, idade_inp, altura_inp, nacionalidade_inp)
print(f"\ncor_de_cabelo:{cor_de_cabelo.pessoa}\nidade:{idade.pessoa}\naltura:{altura.pessoa}\nnacionalidade{nacionalidade.pessoa}")
contador= 1

while contador <= 5:
    print(contador)
    
#ex2///////////////////////////////////////////////////////////////////////////////////////
 
 resposta = ""
 
 while resposta != "sair":
     resposta = input("Digite algo (ou 'sair' para finalizar): ")
     
     print("Você decidiu sair. Programa encerrado.")
     
#ex3///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

adivinhar_numero =random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    # Solicita que o usuário insira um palpite
    palpite = int(input("Digite seu palpite: "))

    if palpite < adivinhar_numero:
        print("O número secreto é maior!")
    elif palpite > adivinhar_numero:
        print("O número secreto é menor!")
    else:
        print("Parabéns! Você adivinhou o número!")
        break
    
    

#ex4/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
 class ContaBancaria:
     def _init_(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.saldo = 1000  # Saldo inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def exibir_informacoes(self):
        print(f"Nome do cliente: {self.nome_cliente}")
        print(f"Saldo atual: R${self.saldo}")
        
#ex5//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
usuario_real = "admin"
senha_correta = "1234"

while True:
    
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    
    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        print("Nome de usuário ou senha incorretos. Tente novamente.")
        
#ex6///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
soma_total = 0

print("Digite números para somar. Para encerrar e ver o total, digite 0.")

while True:
    numero = float(input("Digite um número: "))
    
    if numero == 0:
        break  
    
    soma_total += numero 

print(f"A soma total é: {soma_total}")
