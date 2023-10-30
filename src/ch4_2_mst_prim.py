from vis import PrimVisualizer as Visualizer
import data_sample_cities as dsc

# adjacency matrix - array of array
def build_graph():
  global graph
  graph = {u: dict() for u in range(n_cities)}
  for u,v,w in edges:
    graph[u][v] = w
    graph[v][u] = w
  print(graph)
  print_adj_matrix()

def print_adj_matrix():
  for u in range(n_cities):
    for v in range(n_cities):
      w = f'{graph[u][v]:5d}' if v in graph[u] else ' ....'
      print(w, end='')
    print()
  print()

def main():
  global n_cities
  n_cities = len(cities)

  build_graph()

  start_city_index = 0
  print(f'{n_cities} cities, starts from {cities[start_city_index]}')

  global weights, origins
  weights = dict()
  weights[start_city_index] = 0
  print(weights)

  origins = dict()
  origins[start_city_index] = start_city_index

  global mst
  mst = []
  while weights:
    print('<', weights)
    w, ci = pop_smallest_weight()
    mst.append((origins[ci], ci, w))    
    print('>', weights)

    adjacents = graph[ci]
    for adj in adjacents:
      weight = adjacents[adj]
      weights[adj] = weight
      vis.append(weight, adj, ci)

    if len(mst) <= 1: break

def pop_smallest_weight():
  min_wi = -1
  min_w = float('inf')
  for wi in range(n_cities):
    if wi not in weights: continue
    w = weights[wi]
    if w < min_w:
      min_w = w
      min_wi = wi
  if min_wi >= 0: del weights[min_wi]
  return min_wi, min_w

if __name__ == '__main__':
  vis = Visualizer('Minimum Spanning Tree - Prim')
  idx = 0
  while True:
    cities, edges = dsc.cities, dsc.edges
    vis.setup(vis.get_main_module())
    vis.draw()
    main()
    again = vis.end()
    if not again: break
    if vis.restart_lshift:
      dsc.next()
    elif vis.restart_rshift:
      dsc.random()
