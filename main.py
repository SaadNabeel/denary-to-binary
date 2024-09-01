def decimaltobinary(decimalnumber):
    if decimalnumber == 0:
        return "0"
    binary = ""
    while decimalnumber > 0:
        binary = str(decimalnumber % 2) + binary
        decimalnumber = decimalnumber // 2
    return binary


decimalnumber = int(input("Enter a decimal number: "))
binarynumber = decimaltobinary(decimalnumber)
print("The binary representation of ",decimalnumber,"is",binarynumber)