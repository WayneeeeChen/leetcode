class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        
        strs.sort(key=lambda strs:len(strs))
        prefix = strs[0]
        
        for i in range(len(strs)):
            for index in range(min(len(prefix),len(strs[i]))):
                if prefix[index]!=strs[i][index]:
                    prefix = prefix[0:index]
                    break
        print("longest Common Prefix : "+prefix)
        return prefix

if __name__ == '__main__':
    ExampleList = ["flower","flow","flight"]
    a = Solution()
    a.longestCommonPrefix(ExampleList)