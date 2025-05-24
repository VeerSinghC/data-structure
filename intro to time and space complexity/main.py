def fun1(n):
    return n * (n + 1) //2

def fun2(n):
    total= 0
    for i in range(1, n + 1):
        total  += i
    return total

def fun3(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(i, i + 1):
            count += i * j
    return count

n = 9
print("fun1 result:", fun1(n)) 
print("fun2 result:", fun2(n))  
print("fun3 result:", fun3(n))