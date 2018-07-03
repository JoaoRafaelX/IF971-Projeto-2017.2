
from random import randint
from time import clock
class Ponto:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.movs = [self.cima, self.direita,
                     self.baixo, self.esquerda]


    def movimento(self, r = 0):
        #Gera um número aleatório para a direção
        self.movs[randint(0, 3)]()

    #Todos os movimentos têm um módulo de 25
    def cima(self):
        self.y = (self.y + 1) % 25
    def direita(self):
        self.x = (self.x + 1) % 25
    def baixo(self):
        self.y = (self.y - 1) % 25
    def esquerda(self):
        self.x = (self.x - 1) % 25

class Grid:
    def __init__(self):
        self.a = Ponto()
        self.b = Ponto()
        
        #Como só são 25 distâncias possíveis
        #Ao invés de guardar todas as distâncias obtidas
        #Guarda quantas vezes tal distância apareceu
        #Com isso conseguimos calcular qualquer coisa
        self.contagem = [0]*25        
        self.tempoInicial = 0

    def rodar(self):
        #Guarda o tempo que o programa é iniciado
        self.tempoInicial = clock()
        pausa = 1
        i = 0
        #Roda 100 mil vezes o método de mover 10 mil vezes
        vezes = 100000
        while i < vezes:
            self.dezmil()
            i += 1
            #Nos 1m, 10m, 100m e 1b, faz um print dos dados
            if i == pausa:
                self.printarAtual(i)
                pausa *= 10

    def printarAtual(self, numero):
        tempoAtual = clock()
        tamanho = numero*10000

        media = 0
        #Faz a média com um somatório, como Pedro calculava a Esperança
        for i in range(25):
            media += self.contagem[i] * i
        media /= tamanho

        print(str(tamanho), "iterações")
        print("Média = ", str(media))
        print("Tempo = ", str(tempoAtual - self.tempoInicial) + "s")

        #Mostra a contagem de distâncias
        for i in range(25):
            print(str(i), "\t\t", str(self.contagem[i]))       
        print()
            

    def dezmil(self):
        i = 0
        vezes = 10000
        for i in range(vezes):
            #Move ambos os pontos
            self.a.movimento()
            self.b.movimento()

            #E adiciona +1 na contagem certa
            self.contagem[self.distancia()] += 1

    def distancia(self):
        ax = self.a.x
        ay = self.a.y
        bx = self.b.x
        by = self.b.y

        #ABS não e método de Grafo
        #Faz um módulo |  | da subtração das coordenadas
        #25 - o valor  é para simular uma espelhação
        deltax = min(abs(ax - bx), 25 - abs(ax - bx))
        deltay = min(abs(ay - by), 25 - abs(ay - by))

        return deltax + deltay

    '''
    def distancia(self):
        bx = self.b.x
        by = self.b.y
        #Réplicas do meio, esquerda e direita
        #Com as réplicas do centro, cima e baixo
        todosB = [(bx, by),
                  (bx, (by + 25)),
                  (bx, (by - 25)),
                  ((bx - 25), by),
                  ((bx - 25), (by + 25)),                  
                  ((bx - 25), (by - 25)),
                  ((bx + 25), by),
                  ((bx + 25), (by + 25)),
                  ((bx + 25), (by - 25))]
        
        menor = 24
        coordA = (self.a.x, self.a.y)
        #Calcula a distância do A para todos os Bs
        for i in range(len(todosB)):
            dist = self.calcularDistancia(coordA, todosB[i])
            if dist < menor:
                menor = dist
        return menor
    
    def calcularDistancia(self, a, b):
        #ABS não e método de Grafo
        #Faz um módulo |  | da subtração das coordenadas
        #|3 - 10| + |2 - 3| = 8 
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    '''



###########################                    
g = Grid()
g.rodar()




            
            
        
        
        
