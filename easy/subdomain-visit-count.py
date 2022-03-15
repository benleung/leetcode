'''
10'
'''
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h = defaultdict(int)
        for cpdomain in cpdomains:
            count , domain = cpdomain.split()
            count = int(count)
            
            subdomains = domain.split(".")
            subdomain_strs = []
            for i in range(len(subdomains)):
                subdomain_strs.append(".".join(subdomains[i:]))
            
            for subdomain_str in subdomain_strs:
                h[subdomain_str] += count
                
        ans = []
        for subdomain, count in h.items():
            ans.append("{0} {1}".format(count, subdomain))
        return ans
        