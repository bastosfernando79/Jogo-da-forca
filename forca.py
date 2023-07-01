import random

palavras = ['carro', 'matematica']
palavra_escolhida = random.choice(palavras)

print('Adivinhe a palavra abaixo:')
print("{} ".format('_ '*len(palavra_escolhida)))

aposta = ["y" for i in range(len(palavra_escolhida))]
count_erradas = 6
while count_erradas > 0 or count_certas != len(palavra_escolhida):  

    letra = input("Digite uma letra: ")
    
    aux = 0
    for i in range(len(palavra_escolhida)):
        if letra == palavra_escolhida[i]:
            aposta[i] = letra                        
            aux += 1
    
    count_certas = 0
    for i in range(len(aposta)):
        if aposta[i] == "y":
            print("{} ".format("_ ")) 
        else: 
            print(aposta[i])           
            count_certas += 1

    if aux == 0:
        count_erradas -= 1
   
    print("Chances restantes: {}".format(count_erradas))        
    
    if count_certas == len(palavra_escolhida):
        print("Parabéns! Você ganhou!")
