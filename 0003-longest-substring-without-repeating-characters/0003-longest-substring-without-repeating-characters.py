class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = [-1]*256
        l=0
        r=0
        n=len(s)
        max_len= 0
        while r<n:
            if hash[ord(s[r])]!=-1:
                l=max(l,hash[ord(s[r])]+1)
            hash[ord(s[r])]=r
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len

       