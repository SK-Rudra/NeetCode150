class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        num1=num1+num2
        num1=sorted(num1)
        a=len(num1)//2
        if len(num1)%2==0:
            b=(num1[a-1]+num1[a])/2.0
            return b
        else:
            return num1[a]
    
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """