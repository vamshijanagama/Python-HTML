class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for i in range(len(s)):
            if(97 <= ord(s[i]) <= 122 or 65 <= ord(s[i]) <= 90 or 48 <= ord(s[i]) <= 57):
                if(s[i].isupper()):
                    a = a + s[i].lower()
                else:a=a+s[i]
        i = 0
        j = len(a)-1
        while(i<j):
            if(a[i] != a[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
        

            