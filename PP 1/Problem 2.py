def binaryToDecimal(binaryString):
    binaryString = str(binaryString)
    decimal = 0

    for i in range(len(binaryString)):
        decimal += int(binaryString[i]) * (2 ** (len(binaryString) - i - 1))
    return decimal

print(binaryToDecimal(1010))
print(binaryToDecimal(1111))
print(binaryToDecimal(1))
print(binaryToDecimal(0))

