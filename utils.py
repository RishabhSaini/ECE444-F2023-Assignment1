import os

class Utils:
    def reversed(num):
        if type(num) != int:
            raise TypeError("Inserted num can only be of type int")
        if num < 0:
            return -1*int(str(num)[1:][::-1])
        return int(str(num)[::-1])
    
    def formatter(num):
        if type(num) != int:
            raise TypeError("Inserted num can only be of type int")       
        return bin(num), oct(num)
