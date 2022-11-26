


# Prime number:
'''
def Prime(n):
    if n>1:
        for i in range(2,n): #2,10
            if n%i == 0: #11%2 = 0
                return ("Not Prime")
        else:
            return ("Prime")
    return("Not Prime")
n = int(input()) # 11
Prime(n)

'''


# home work: for loop use kore "I Love you Bangladesh" word ti 25 bar output a prodorshon kora.

# home work: for loop use kore 200 theke 0 te asa lagbe and protibar count hobe 1.


'''arr = list(map(int,input().split()))
print(arr)
'''
'''a,b,c = map(int,input().split())
print(a,b,c)'''

# Two list to one Dictionary

'''
one_list = [12,3,4]
two_list = ["Mango","Orange","Banana"]
dictionary = {}
for i in range(len(one_list)):
    dictionary[two_list[i]] = one_list[i]
print(dictionary)

'''
for i in range(int(input())):
    def twos_comp(val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits +1))) != 0: # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)        # compute negative value
        return val
    a = int(input())
    print(twos_comp(a,128))












