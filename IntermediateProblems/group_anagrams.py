class Solution(object):
    def groupAnagrams(self, strs):
        hash = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))

            if sorted_i not in hash:
                hash[sorted_i] = []

            hash[sorted_i].append(i)
        
        return list(hash.values())
            
            

