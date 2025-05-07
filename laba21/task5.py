def sieve(lst):
    unique_elements = []
    for element in lst:
        if element not in unique_elements:
            unique_elements.append(element)
    unique_elements.reverse()
    return tuple(unique_elements)
exapmple  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(exapmple)
print(sieve(exapmple))