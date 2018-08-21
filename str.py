alist = input("yek list vared konid: ")
alist = alist.split()

astr = input("yek str vared konid: ")

def rep(alist , astr):
    for i in range(1,4):
        alist[i] = astr
    return alist

print(rep(alist , astr))