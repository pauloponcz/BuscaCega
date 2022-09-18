
def printVert(d,N,inicio,fim,nomes):
    print("\n-----Resultado:-----")
    for i in range(N):
        if i == fim:
            print("Tempo até encontrar",nomes[i],":",d[i],"\n")

def loadlista():
    arquivo = open('Grafo.txt','r')
    lista = arquivo.readlines()  #ler todas as linhas
    for i in range (len(lista)):
        linha = lista[i].split()
        if i == 0:
            N=int(linha[0])
            lista_adj = [[]for x in range(N)]    # criando a lista em branco com o tamanho certo

            #print("-----------------\n",lista_adj)
        else:
            lista_adj[int(linha[0])].append(int(linha[1]))   # colocando os adjacentes na lista

            #print("-----------------\n",lista_adj)
    arquivo.close
    return lista_adj,N


def DFS_visit(u,fim):
    aux = 0
    global tempo
    tempo = tempo + 1
    tempIda[u] = tempo
    cor[u] = "Cinza"
    if cor[fim] == "Cinza" and tempo == tempIda[fim]:
        print("Achou -----> Vertice:",u,"cor:",cor[u],"\n---------------------")
    else:
         print("Vertice:",u,"cor:",cor[u],"\n---------------------")
    for v in lista_adj[u]:
        if cor[v] == "Branco":
            DFS_visit(v,fim)
    cor[u] = "Preto"
    tempo = tempo +1
    tempVolta[u] = tempo
    print("Vertice:",u,"cor:",cor[u],"\n---------------------")

def DFS(fim):
    for u in Vertice:
        cor[u] = "Branco"
    for u in Vertice:
        if cor[u] == "Branco":
            DFS_visit(u,fim)

def HUB(nomes):
    print("========================================")
    print('|Seja bem vindo a busca em profundidade|')
    print("========================================")
    print('Escolha de qual pessoas vc deseja começar e Escolha outra para que ela ache')
    cont = 0
    for i in nomes:
        print(cont,'-',i)
        cont+=1
    inicio = int(input('Escolha a pessoa do seu ponto inicial: '))
    fim = int(input('Escolha qual pessoa ela deve encontrar: '))
    return inicio,fim
    

[lista_adj,N]= loadlista()
# cria as variaveis com o tamanho exato de vertices
cor = [0]*N
tempIda = [0]*N
tempVolta = [0]*N
tempo = 0
nomes = ['Hellen','Ana','Lucas','João','Fabio','Amanda']
[inicio,fim] = HUB(nomes)
if inicio == 0:
    Vertice = [0,1,4,3,2,5]
elif inicio == 1:
    Vertice = [1,4,3,0,2,5]
elif inicio == 2:
    Vertice = [2,5,4,3,0,1]
elif inicio == 3:
    Vertice = [3,0,1,4,2,5]
elif inicio == 4:
    Vertice = [4,3,0,1,2,5]
else:
    Vertice = [5,0,1,4,3,2]
DFS(fim)
printVert(tempIda,N,inicio,fim,nomes)