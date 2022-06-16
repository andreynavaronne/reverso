palavra = input ('Por favor, escreva uma palavra: ')
len_palavra = len(palavra)
listaPalavra=[]
reverso=""
for i in range(len_palavra):
    listaPalavra.append(palavra[i])

for j in range(len_palavra):
    reverso = listaPalavra[j] + reverso

print(reverso)