


# Prime number:

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













