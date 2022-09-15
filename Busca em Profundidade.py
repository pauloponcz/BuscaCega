
def printVert(d,f,N):
    for i in range(N):
        print("Vértice",i,":","Ida:",d[i],"Volta:",f[i])

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


def DFS_visit(u):
    global tempo
    tempo = tempo + 1
    tempIda[u] = tempo
    cor[u] = "Cinza"

    print("Vertice:",u,"cor:",cor[u],"\n---------------------")
    for v in lista_adj[u]:
        if cor[v] == "Branco":
            DFS_visit(v)
    cor[u] = "Preto"
    tempo = tempo +1
    tempVolta[u] = tempo
    print("Vertice:",u,"cor:",cor[u],"\n---------------------")

def DFS():
    for u in Vertice:
        cor[u] = "Branco"
    for u in Vertice:
        if cor[u] == "Branco":
            DFS_visit(u)

[lista_adj,N]= loadlista()
Vertice = [0,1,4,3,2,5]
# cria as variaveis com o tamanho exato de vertices
cor = [0]*N
tempIda = [0]*N
tempVolta = [0]*N
tempo = 0       
DFS()
printVert(tempIda,tempVolta,N)