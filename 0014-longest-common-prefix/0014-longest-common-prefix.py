class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string_prefix = ""
        i_string = -1
        for i in range(min(list(map(lambda x: len(x), strs)))):
            for i_string in range(len(strs)-1):
                # print(f"[{i}] current string:{strs[i_string]}")
                if strs[i_string][:i+1] != strs[i_string+1][:i+1]:
                    return string_prefix
            string_prefix = strs[i_string][:i+1]
        return string_prefix