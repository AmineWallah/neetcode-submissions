class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexes = {}
        for i, word in enumerate(strs):
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            if sorted_word not in indexes:
                indexes[sorted_word] = [i]
            else:
                indexes[sorted_word].append(i)

        result = []
        for key, value in indexes.items():
            group = []
            for index in value:
                group.append(strs[index])

            result.append(group)

        return result
        