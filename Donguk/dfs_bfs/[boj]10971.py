'''
Traveling Salesman problem (TSP)
어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획
단, 한 번 갔던 도시로는 다시 갈 수 없다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0
'''
N = int(input())
budget = [list(map(int, input().split())) for _ in range(N)]


bfs