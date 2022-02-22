'''
print("Xin chào", end=". ", sep="_")
print("****")
print(2**3)
print(10**(1/2))
'''
#x, y = map(int, input().split())
#(%.02)
n = "30"
print(n * 3, type(n * 3))  
m = list(map(int, input().split()))
m.sort()
m.reverse()
print(m)
def gt(n):
    r = 1 
    for i in range(1, n + 1):
        r *= i
    return r

print(gt(5))