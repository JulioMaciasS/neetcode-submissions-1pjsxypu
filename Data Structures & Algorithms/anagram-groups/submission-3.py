class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for  val in strs:
            key = tuple(sorted(val))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key] += [val]
        
        finalList = []

        for value in hash_map.values():
            finalList.append(value)
        
        return finalList
