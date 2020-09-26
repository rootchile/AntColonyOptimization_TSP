import math

from aco import ACO, Graph
from plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    cities = []
    points = []
    with open('./data/chn31.txt') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
            points.append((int(city[1]), int(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)

    ants = 10
    iterMax = 1000
    alpha = 1.0
    beta = 10.0
    rho = 0.6
    aco = ACO(ants, iterMax, alpha, beta, rho, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)

    print("------------------------------------------------------------------------------")

    print(f'ants: {ants}, alpha: {alpha}, beta: {beta}, evaporacion (rho): {rho} ')
    print("Best result:")
    print('cost: {}, path: {}'.format(round(cost,0), path))
    plot(points, path)

    print("------------------------------------------------------------------------------")


    ants = 5
    iterMax = 10
    alpha = 1.0
    beta = 2.0
    rho = 0.3
    aco = ACO(ants, iterMax, alpha, beta, rho, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)

    print("------------------------------------------------------------------------------")

    print(f'ants: {ants}, alpha: {alpha}, beta: {beta}, evaporacion (rho): {rho} ')
    print("Best result:")
    print('cost: {}, path: {}'.format(round(cost,0), path))
    plot(points, path)

    print("------------------------------------------------------------------------------")

    ants = 10
    iterMax = 10
    alpha = 2.0
    beta = 0.5
    rho = 0.7
    aco = ACO(ants, iterMax, alpha, beta, rho, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)

    print("------------------------------------------------------------------------------")

    print(f'ants: {ants}, alpha: {alpha}, beta: {beta}, evaporacion (rho): {rho} ')
    print("Best result:")
    print('cost: {}, path: {}'.format(round(cost,0), path))
    plot(points, path)

    print("------------------------------------------------------------------------------")

    ants = 20
    iterMax = 10
    alpha = 1.0
    beta = 15.0
    rho = 0.7
    aco = ACO(ants, iterMax, alpha, beta, rho, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)

    print("------------------------------------------------------------------------------")

    print(f'ants: {ants}, alpha: {alpha}, beta: {beta}, evaporacion (rho): {rho} ')
    print("Best result:")
    print('cost: {}, path: {}'.format(round(cost,0), path))
    plot(points, path)

    print("------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()
