class Solution(object):
    def romanToInt(self, str):
       roman_values = {
           "I":1 , "V" :5 , "X":10 ,"L":50 , "C":100 , "D":500 ,"M":1000
       }
       toatl = 0
       prev_value = 0
       for char in reversed(str):



