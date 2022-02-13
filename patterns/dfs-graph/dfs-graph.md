### represent graph using python
see notion [graph theory]


### graph tranverse using iteration

classic example: accounts-merge

```python
seen = set()
ans = []
em_to_name = {}
em_graph = defaultdict(set)

# here we use loop to traverse all unconnected
# components of the graph
for email in em_graph:
    if email not in seen:
        seen.add(email)
        st = [email]
        component = []
        
        # this loop give us the all conneted path as here
        # all common gmail as a list in comonent
        while st:
            edge = st.pop()
            component.append(edge)
            for nei in em_graph[edge]:
                if nei not in seen:
                    seen.add(nei)
                    st.append(nei)
                    
        # after geting all connect comonent
        # we sorted the as question
        # and search the owner of the starting email
        # append in the ans
        ans.append([em_to_name[email]] + sorted(component))

```

### Example: Find Path

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
