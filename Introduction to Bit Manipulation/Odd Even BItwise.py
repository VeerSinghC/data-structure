def isEvenOdd(n):
    if (n ^ 1 == n+1):
        return True;
    else:
        return False;

number = int(input("Enter a number: "))

if isEvenOdd(number):
 print(number, "is an even number")
else:
 print(number, "is an odd number")        