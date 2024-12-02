"""
Implementar um programa na linguagem de sua escolha, que permita a representação em memória de um grafo.

Este programa deve permitir a entrada dos vértices e os pesos das arestas, considere as seguintes funcionalidades:

1. Permitir o armazenamento de até 20 vértices

2. Fazer a leitura dos pesos das arestas de cada vértice

3. Considerar sempre pesos de arestas positivos

4. Mostrar os dados armazenados
"""

class Grafo:
    def __init__(self):
        self.vertices = []
        self.pesos = {}

    def adicionar_vertice(self, vertice):
        if len(self.vertices) <= 20:
            self.vertices.append(vertice)
            self.pesos[vertice] = {}

    def adicionar_peso(self, origem, destino, peso):
        if peso <= 0:
            print("Peso deve ser positivo")
            return
        self.pesos[origem][destino] = peso

    def ler_pesos(self, vertice):
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            return self.pesos[index]
        return None

    def mostrar_dados(self):
        for i in range(len(self.vertices)):
            print(f"Vertice: {self.vertices[i]}")
            print(f"Pesos: {self.pesos[i]}")
            print()

"""
Implementar um programa para calcular os caminhos mínimos
entre os vértices de um Grafo utilizando o algorítmo de Dijsktra.

1. Permitir o armazenamento de até 20 vértices

2. Fazer a leitura dos pesos das arestas de cada vértice

3. Considerar sempre vértices positivos

4. Mostrar o caminho mínimo entre dois vértices solicitados
"""

def dijkstra(grafo, origem):
    vertices = grafo.vertices
    pesos = grafo.pesos
    distancias = {vertice: float('inf') for vertice in vertices}
    distancias[origem] = 0
    visitados = {vertice: False for vertice in vertices}

    for _ in range(len(vertices)):
        u = min((vertice for vertice in vertices if not visitados[vertice]), key=distancias.get)
        visitados[u] = True

        for vizinho, peso in pesos[u].items():
            if not visitados[vizinho] and distancias[u] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[u] + peso

    return distancias


grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_vertice('E')

grafo.adicionar_peso('A', 'B', 10)
grafo.adicionar_peso('A', 'C', 20)
grafo.adicionar_peso('B', 'D', 15)
grafo.adicionar_peso('C', 'D', 30)
grafo.adicionar_peso('D', 'E', 10)
grafo.adicionar_peso('E', 'A', 50)

distancias = dijkstra(grafo, 'A')
print(distancias)

"""
Resultados:
caminho de A para B: 10
caminho de A para C: 20
caminho de A para D: 25, vai de A para B e depois de B para D
caminho de A para E: 35, vai de A para B, de B para D e de D para E

"""