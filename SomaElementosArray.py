'''
simples soma os dados dentro da lista
soma = 0
l = (1,2,3)
for i in range(len(l)):
    soma += l[i]
print(soma)

'''

'''
#função soma elementos
def somarElementos():
    vetor = []
    count = 0
    #entrada do tamanho do vetor
    tamanho = int(input("Digite o tamanho do vetor: "))
    #entrada de dados
    for i in range(tamanho):
        #mensagem que fica aparecendo pra digitar o dado no vetor
        vetor.append(input("Digite o "+str(i+1)+"° numero: "))

    for j in range(tamanho):
        #soma os dados
        count += int(vetor[j])
        #printa o vetor
        print(vetor[j])
    print("Total da soma é: "+str(count))


if __name__ == '__main__':
    somarElementos()
    
'''


def somarElementos():
    vetor = []
    count = 0
    tamanho = int(input())
    for i in range(tamanho):
        vetor.append(input())
    for j in range(tamanho):
        count += int(vetor[j])
    print(str(count))


if __name__ == '__main__':
    somarElementos()