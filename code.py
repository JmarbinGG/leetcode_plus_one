class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            digits[0] += 1
            if len(str(digits[0])) == 2:
                str(digits[0]).split()
                return list(map(int, str(digits[0])))
        else:
            last = digits[-1]
            last += 1
            digits[-1] = last
        return digits
        
