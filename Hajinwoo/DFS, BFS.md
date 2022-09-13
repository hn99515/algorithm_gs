|             | BFS (너비 우선 탐색)                                                            | DFS (깊이 우선 탐색)                                               |
|:-----------:| ------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **노드**      | 시작 노드와 같은 거리에 있는 노드를 우선으로 방문.                                             | 시작노드에서 선택한노드로 갈 수 있는만큼 가고, 그 후 가장 위의 선택하지 않았던 노드로 이동해 다시 방문. |
| **사용 자료구조** | 큐 Queue                                                                   | 스택 Stack                                                     |
| **시간복잡도**   | list.pop(0)와 append를 썼을 때 : O(N) <br/>해결방법 : collections 라이브러리의 deque 이용. | 쉽게 pop()과 append() 사용하자..                                    |
|             | 선입선출                                                                      | 후입선출                                                         |

-BFS

```python
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```

-DFS

```python
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```
