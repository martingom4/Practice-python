'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        '''
        que es lo que pense es que tengo que encontrar el prefijo comun mas largo entre un array de strings
        si no hay prefijo comun, devolver un string vacio

        '''
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

# Time complexity: O(n*m) where n is the number of strings and m is the length of the shortest string
# Space complexity: O(1) since we are not using any extra space

