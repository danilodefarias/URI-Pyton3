maior=int(input())
menor=int(input())
total=0

#ordenando os números em uma lista
lista = [maior,menor]
lista.sort()
maior = lista[1]
menor = lista[0]

#condição necessária para números pares
if menor%2 == 0:
    menor = menor + 1
    for n in range(menor,maior,2):
        total = total + n #ou total += n
        #use aquio o comando 'print('lista dos números %d somados' %n)' para saber quais números você está somando
    print(total)

#condição necessária para números ímpares
elif menor %2 != 0:
    menor = menor + 1
    for n in range(menor + 1, maior, 2):
        total = total + n  # ou total += n
        #use o aqui o comando 'print('lista dos números %d somados' %n)' para saber quais números você está somando
    print (total)


