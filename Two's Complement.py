
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












