def isSubset(a, b):
    # check input
    a = set(a) # O(len(a))
    b = set(b) # O(len(b))

    # iterate through b as a set to check if the element is in a
    for element in b:  # O(len(b)) 
        if element not in a:
            return False
    # return True if all elements in a
    return True
# print(isSubset(['A','B','C','D','E'], ['A','E','D']))
# print(isSubset(['A','B','C','D','E'], ['A','D','Z']))
# print(isSubset(['A','D','E'], ['A', 'A','D','E']))

# Time: O(M+N); Space: O(M+N)