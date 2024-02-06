import networkx as nx
import heapq

class Dijkstra_heap_Graph(nx.Graph):
    def dijkstra(self, start_node_name):
        distances = {vertex: float('infinity') for vertex in self}
        distances[start_node_name] = 0

        heap_queue = [(0, start_node_name)]   # Початкова точка відліку відстаней

        while len(heap_queue) > 0:
            current_node = heapq.heappop(heap_queue)
            if current_node[0] > distances[current_node[1]]:
                continue
            #print(current_node[0], current_node[1],self.edges.data('weight', nbunch=[current_node[1]]))
            for _, neighbor, weight in self.edges.data('weight', nbunch=[current_node[1]]):
                distance = current_node[0] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap_queue, (distance, neighbor))
        return distances

def main():
    # Граф деяких автошляхів Европи
    G = Dijkstra_heap_Graph()
    G.add_nodes_from(['Київ', 'Варшава', 'Прага', 'Братислава', 'Відень', 
                    'Будапешт', 'Рим', 'Париж', 'Берлін', 'Лондон', 'Мадрид'])
    G.add_edges_from([('Київ', 'Будапешт'), ('Київ', 'Братислава'), ('Київ', 'Прага'),
                    ('Київ', 'Варшава'), ('Прага', 'Відень'), ('Прага', 'Варшава'),
                    ('Прага', 'Рим'), ('Прага', 'Берлін'), ('Прага', 'Париж'),
                    ('Відень', 'Братислава'), ('Відень', 'Будапешт'), ('Відень', 'Рим'),
                    ('Будапешт', 'Братислава'), ('Будапешт', 'Рим'), ('Рим', 'Париж'),
                    ('Рим', 'Мадрид'), ('Варшава', 'Берлін'), ('Берлін', 'Париж'),
                    ('Берлін', 'Лондон'), ('Лондон', 'Париж'), ('Лондон', 'Мадрид'),
                    ('Мадрид', 'Париж')
                        ])
    G['Київ']['Будапешт']['weight'] = 1117
    G['Київ']['Братислава']['weight'] = 1330
    G['Київ']['Прага']['weight'] = 1409
    G['Київ']['Варшава']['weight'] = 794
    G['Прага']['Відень']['weight'] = 340
    G['Прага']['Варшава']['weight'] = 640
    G['Прага']['Рим']['weight'] = 1300
    G['Прага']['Берлін']['weight'] = 351
    G['Прага']['Париж']['weight'] = 1031
    G['Відень']['Братислава']['weight'] = 78
    G['Відень']['Будапешт']['weight'] = 244
    G['Відень']['Рим']['weight'] = 1134
    G['Будапешт']['Братислава']['weight'] = 200
    G['Будапешт']['Рим']['weight'] = 1215
    G['Рим']['Париж']['weight'] = 1422
    G['Рим']['Мадрид']['weight'] = 1957
    G['Варшава']['Берлін']['weight'] = 574
    G['Берлін']['Париж']['weight'] = 1057
    G['Берлін']['Лондон']['weight'] = 1101
    G['Лондон']['Париж']['weight'] = 461
    G['Лондон']['Мадрид']['weight'] = 1721
    G['Мадрид']['Париж']['weight'] = 1275

    city = 'Київ'
    shortest_distances = G.dijkstra(city)

    print(f'Найкоротший шлях між вершиною {city} та іншими вершинами графу')
    print('|       Город       | Найкоротший шлях, км   |')
    print('|-------------------|------------------------|')
    for city_name, dist in shortest_distances.items():
        print(f'| {city_name:17} | {dist:^22} |')

if __name__ == '__main__':
    main()