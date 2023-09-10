L = "1*2-2*1+7*5-56+4*5"
ListOperation = ['#']
ListNum = []
l = len(L)
s = 0
i = 0
WeightDIct = {'+': 1, '-': 1, '*': 2, '#':3}
while 1:
    if '0' <= L[i] <= '9':
        ListNum.append(int(L[i]))
        i += 1

    elif WeightDIct[L[i]] < WeightDIct[ListOperation[-1]]:
        ListOperation.append(L[i])
        i += 1
    else:
        k = ListNum.pop()

        if L[i] == '+':
            temp = k + int(L[i + 1])

        elif L[i] == '-':
            temp = k - int(L[i + 1])
        else:
            temp = k * int(L[i+1])
        opea=ListOperation.pop()
        k = ListNum.pop()
        if opea == '+':
            temp1 = k + temp
        elif opea == '-':
            temp1 = temp - k
        else:
            temp1 = k * temp
        ListNum.append(int(temp1))
        i += 2
    if i==l:
        break
print(ListNum[-1])