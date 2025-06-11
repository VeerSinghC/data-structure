def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal

number = int(input("Enter a binary number: "))
print(f"The decimal equivalent of {number} is {binary_to_decimal(str(number))}")