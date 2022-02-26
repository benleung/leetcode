# represent graph using python
other advanced knowledge: see notion [graph theory]


# Build Up Graph Data
![picture 7](images/2148a4c895d49c8e88cfb6bbfe2eb8f68dfb5223d02302e09b3cd7da2266d287.png)  
## Data Representation
```python
graph = {'A': {'B', 'C'},
        'B': {'C', 'D'},
        'C': {'D'},
        'D': {'C'},
        'E': {'F'},
        'F': {'C'}}
# keys of graph are called "edge"
```
## Convert array to all directly connected
![picture 10](images/0e22907f9debd501301d709fb611d412a738bf0087b194604496bca8b3e92efe.png)  
```python
emails = ['A','B','C']
graph = defaultdict(set)
for email in emails:
    graph[email] |= emails  # -email if not include self-loop
```

## Convert array to all indirectly connected
![picture 9](images/5c07cd5e9e4e5374597bd3fd6dfc3363e9bdc122a5d92d3178415052ee22f24e.png)  
```python
emails = ['A','B','C']
graph = defaultdict(set)
for email in emails:
    graph[a[1]].add(email)
    graph[email].add(a[1])
```



# DFS Transversal of graph (using iteration)
example: accounts-merge

```python
seen = set()  # point 2: avoid visited
ans = []
em_to_name = {}
em_graph = defaultdict(set)

# point 1: try all the nodes
for email in em_graph:
    if email not in seen: # point 2: avoid visited
        st = [email]
        seen.add(email) # point 2: avoid visited (right after addtion to stack)

        # point 4: actions for this cluster here
        component = []
        
        while st:
            edge = st.pop()

            component.append(edge)

            for nei in em_graph[edge]: # point 3: explore next
                if nei not in seen: # point 2: avoid visited
                    seen.add(nei) # point 2: avoid visited (right after addtion to stack)
                    st.append(nei)
                    
        # point 4: actions for this cluster here
        ans.append([em_to_name[email]] + sorted(component))

```

### Example: find-path

```python

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:  # normally won't happen
            return None
        for node in graph[start]:  # divide into subproblems
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath  # skip unsuccessful paths
        return None

>>> find_path(graph, 'A', 'D')
    ['A', 'B', 'C', 'D']
    >>>
```
