def nott(a):
    return not a

def andd(a,b):
    return a and b

def orr(a,b):
    return a or b

# We built xor using the logical connectives that are allowed, so we can use this function for simplicity in our formula
def xor(a, b):
    return orr(andd(a, nott(b)), andd(nott(a), b))

# takes in binary strings A0A1, A2A3, and A5A6A7 and returns a 7-tuple corresponding to the truth assignments of their digits
def binaryStringsToTruthAssignment(n, m, sum):
    a0, a1 = bool(int(n[0])), bool(int(n[1]))
    a2, a3 = bool(int(m[0])), bool(int(m[1]))
    a5, a6, a7 = bool(int(sum[0])), bool(int(sum[1])), bool(int(sum[2]))
    return(a0, a1, a2, a3, a5, a6, a7)

# takes in binary strings A0A1, A2A3, and A5A6A7 and returns the truth value of our formula using the corresponding truth assignments of digits
def formula(n, m, sum):
    (a0, a1, a2, a3, a5, a6, a7) = binaryStringsToTruthAssignment(n, m, sum)
    # doubleOnes checks whether both a0 and a3 are 1 (carry 1 to the 2nd digit)
    doubleOnes = andd(a1, a3)
    # a7check1 checks whether a7 is the correct bool in the case that not both of a0 and a3 are 1
    a7check1 = andd(nott(doubleOnes), orr(andd(a7, orr(a1, a3)), andd(nott(a7), nott(orr(a1, a3)))))
    # a7check2 checks whether a7 is the correct bool in the case that both a0 and a2 are 1
    a7check2 = andd(doubleOnes, nott(a7))
    # x1 checks if a0 = a2 = 1, a5 = 1, and a6 = 0 (for situation when 1 is not carried, 1 + 1 = 10)
    x1 = andd(andd(a0, a2), andd(a5, not(a6)))
    # x2 checks if one of a0, a2 is 1, a5 = 0, a6 = 1 (for the situation when 1 is not carried, 1 + 0 = 01)
    x2 = andd(xor(a0, a2), andd(nott(a5), a6))
    # x3 checks if a0 = a2 = a5 = a6 = 0 (for situation when 1 is not carried, 0 + 0 = 00)
    x3 = andd(nott(orr(a0, a2)), nott(orr(a5, a6)))
    # route1 checks the formula in the case that not both of a0 and a3 are 1
    route1 = andd(a7check1, orr(orr(x1, x2), x3))
    # y1 checks if a0 = a2 = a5 = a6 (for situation when 1 IS carried, 1 + 1 + 1 = 11)
    y1 = andd(andd(a0, a2), andd(a5, a6))
    # y2 checks if one of a0, a2 is 1, a5 = 1, a6 = 0 (for situation when 1 IS carried, 1 + 0 + 1 = 10)
    y2 = andd(xor(a0, a2), andd(a5, nott(a6)))
    # y3 checks if a0 = a2 = 0, a5 = 0, a6 = 1 (for situation when 1 IS carried, 0 + 0 + 1 = 01)
    y3 = andd(nott(orr(a0, a2)), andd(nott(a5), a6))
    # route2 checks the formula in the case that both a0 and a3 are 1
    route2 = andd(a7check2, orr(orr(y1, y2), y3))
    # returns formula for all cases combined
    return route1 or route2

# takes in binary strings A0A1, A2A3, and A5A6A7 and checks if the sum is correct in binary    
def checkSumBinaryString(n, m, sum):
    return int(n, 2) + int(m, 2) == int(sum, 2)

# twoDigits is a list of all possible values of A0A1 (and A2A3)
# threeDigits is a list of all possible values of A5A6A7
# I build these lists recursively

digits = ['0', '1']
twoDigits = []
for d in digits:
    twoDigits.append(d + "0")
    twoDigits.append(d + "1")
threeDigits = []
for d in twoDigits:
    threeDigits.append(d + "0")
    threeDigits.append(d + "1")

# checks if our formula correctly checks the sum in all cases
def checkValid():
    for n in twoDigits:
        for m in twoDigits:
            for sum in threeDigits:
                if formula(n, m, sum) != checkSumBinaryString(n, m, sum):
                    return False
    return True

print(checkValid())