listt = input("voroodi ha ra be fasele yek space vared konid: ")
listt = listt.split()
def boresh(listt):
    output=[]
    tool = len(listt)
    output.append(listt[0])
    for i in range(1, tool):
        if i % 2 == 0:
            output.append(listt[i])
    return output
print(boresh(listt))
