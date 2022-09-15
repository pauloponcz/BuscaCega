print('=============================================')
print('         Busca por largura')
print('=============================================')

#Armazena a qnt de noh que tem o grafo
nohs = int(input('Digite a quantidade de pontos: '))
viseted = []
graph = []

#Define falso para todas as posicoes e obtem as ligacoes de um noh especifico
for i in range(nohs):
    viseted.append(False)
    print('=============================================')
    x = int(input("\nDigite a quantidade de nohs que tem o noh {} :\n".format(i)))
    connected = []
    for j in range(x):
        y = int(input("Digite os nohs que estao conectados ao noh {} :".format(i)))
        connected.append(y)

    graph.append(connected)
print('\n=============================================')
       

#Faz a busca para um determinado noh
queue = []
queue.append(int(input('Digite de onde deve comecar: ')))

print('=============================================\n')
end = int(input('Digite onde deve parar: '))

print('=============================================\n')


while len(queue) > 0:
    nodo = queue.pop(0)
    viseted[nodo] = True
    print(nodo)

    if nodo == end:
        break
    for i in graph[nodo]:
        if viseted[i] == False:
            viseted[i] = True
            queue.append(i)

print('Vc chegou a seu destino!')