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
        self.pesos = []

    def adicionar_vertice(self, vertice):
        if len(self.vertices) < 20:
            self.vertices.append(vertice)
            self.pesos.append([])

    def adicionar_peso(self, vertice, peso):
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            self.pesos[index].append(peso)

    def mostrar_dados(self):
        for i in range(len(self.vertices)):
            print(f"Vertice: {self.vertices[i]}")
            print(f"Pesos: {self.pesos[i]}")
            print()

grafo = Grafo()
grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(3)
grafo.adicionar_peso(1, 10)
grafo.adicionar_peso(1, 20)
grafo.adicionar_peso(2, 30)
grafo.adicionar_peso(3, 40)
grafo.mostrar_dados()

# Output:
# Vertice: 1
# Pesos: [10, 20]
