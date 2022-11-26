




'''
# Function Structure:
def function_name(parameter):
    return variable

# Main Driver:
# input
# function call and parameter pass
'''



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

# output format:

# 1. 3rd maximum number:

#print(sorted(list(map(int,input().split())))[-3])

#from collections import Counter

'''arr = ["a","b","a","b","c","d"]
res = []
for i in arr:
    res[i] = arr.count(i)
print(res)
'''


# Data Type Check:

'''
a = 3.4
b = 3
c = "34445"
d = [2,3]
e = (2,4,5)
f = {3,5,5}
g = {"a":3,"b":4}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
'''

# Even or Odd nirnoy.
'''
n = int(input()) # 13838883
if n%2 == 0:
    print("Even")
else:
    print("Odd")
'''
'''
n = int(input())
print(int(str(n)[-1]))
if int(str(n)[-1])%2 == 0:
    print("Even")
else:
    print("Odd")

'''



'''
testcase = int(input()) #544845848488484848484848
while 1<=testcase:
    print("even") if int(input())%2 == 0 else print("odd")
    testcase -= 1

'''
'''
testcase = int(input()) # test case limit
for i in range(testcase): # for _ in range(int(input())):
    print("even") if int(input()) % 2 == 0 else print("odd")
'''

# Today we are learning For Loop use ot python:
# for loop statement:
# namota:
'''
n = int(input("Enter your any namota number: ")) #10
for i in range(1,11):
    print("%d X %d = %d"%(n,i,n*i))
    
'''


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
// Two's complement number 

for i in range(int(input())):
    def twos_comp(val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits +1))) != 0: # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)        # compute negative value
        return val
    a = int(input())
    print(twos_comp(a,128))












