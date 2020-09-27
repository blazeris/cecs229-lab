"""
Programming Assignment 1
Problem 1
Nathan Lai
"""

def euclideanAlgorithm(a, b):
    # Base case
    if a is 0:
        return b
    # Base case
    if b is 0:
        return a

    r = max(a, b) % min(a,b)

    # Base case
    if r is 0:
        return min(a, b)

    # Recursive call
    return euclideanAlgorithm(min(a, b), r)

print(euclideanAlgorithm(0, 0))
print(euclideanAlgorithm(465, 0))
print(euclideanAlgorithm(91, 287))