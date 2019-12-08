from typing import List

'''
__author__ = "Tuhin Gupta"

'''

class StringReverse:

    def __init__(self, s: str):
        self.s = s
        self.stringSlice()
        print(StringReverse.reverse(s))
    
    ''' Way 1: reverse using inbuilt slice '''
    def stringSlice(self):
        s = self.s
        print(s[::-1])
    
    ''' Way 2: reverse using recursion '''
    @staticmethod
    def reverse(s):
        if(len(s) == 0):
            return s
        else:
            return StringReverse.reverse(s[1:]) + s[0] 



if __name__ == "__main__":
    StringReverse("This is a string")
