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
    
    #ex4////////////////////////////////////////////////////