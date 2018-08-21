n = int(input("Enter length of the list"))
l1 = []
for i in range(n):
    a = input()
    if(a.isdigit()):
        l1.insert(i, float(a))  # statement1
    else:
        l1.insert(i, a)  # statement2
print(l1)