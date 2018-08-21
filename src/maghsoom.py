voroodi = input("yek adad vared konid: ")
x = int(voroodi)
list = []
#define function
def maghsoom(x):
    for i in range(1,x+1):
        if x % i == 0:
            list.append(i)
    return(list)
print(maghsoom(x))