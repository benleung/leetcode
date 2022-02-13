'''
1 hr

special method, but too slow
should use graph

'''

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.N = len(accounts)
        h = [None] * self.N # [(set, isVisited)]
        sol = []
        
        for i in range(self.N):
            h[i] = [set(accounts[i][1:]), False]
        
        ptr, depth = 0, 0
        for i in range(self.N):
            if not h[i][1]: # not visited yet
                h[i][1] = True
                emails = accounts[i][1:]
                for targetEmail in emails:
                    self.dfs(h, emails, targetEmail)
                sol.append([accounts[i][0]] + sorted(list(set(emails))))
                
            
        return sol
    
    def dfs(self, h, emails, targetEmail):
        for i in range(self.N):
            if not h[i][1] and targetEmail in h[i][0]:
                emails.extend(list(h[i][0]))
                h[i][1] = True
                for nextEmail in h[i][0]:
                    self.dfs(h, emails, nextEmail)

'''
dfs graph transverse (recusion)
'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # dfs function
        def dfs(s,comp):
            if s in seen:
                return
            seen.add(s)
            comp.append(s)
            for nei in em_graph[s]:
                if nei not in seen:
                    dfs(nei,comp)    
            return comp  
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                component = []
                dfs(email, component)
                ans.append([em_to_name[email]] + sorted(component))
                
        return ans 

'''


Time complexity: O(NK \log{NK})O(NKlogNK)
Space complexity: O(NK)O(NK)


dfs graph transverse (iteration)
'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        em_to_name = {}
        em_graph = defaultdict(set)
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                em_graph[acc[1]].add(email)  # no need completely connect all nodes, just use one as representative (acc[1]) is ok
                
                #connect 2nd to 1st email
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name   # technique tag each node with a name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
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
        return ans
