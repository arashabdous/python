def reverse2(s):
	return s[::-1]

def ispal(s):
    rev = reverse2(s)

    if (s == rev):
        return True
    return False

s = input("input: ")
resalt = ispal(s)

if resalt == 1:
    print("yes")
else:
    print(reverse2(s))
