def swap_reverse (voroodi):
    voroodi_swap = voroodi.swapcase()
    voroodi_reverse = voroodi_swap[::-1]
    return voroodi_reverse

x = input("input a string: ")
print(swap_reverse(x))