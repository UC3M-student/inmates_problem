import random as rd

inmates = range(1,101,1)
boxes = rd.sample(range(1,101,1),100)

boxes_required = [(inmates[i],boxes[i-1]) for i in range(100)]

l = 0
for i in inmates:
    x = 0
    inmates = boxes_required[i - 1][1]
    
    while x < 51:
        if i == inmates:
            x = 51
            l = l + 1
            #print("AAAAAAAAAAAALELUYA ",l," AAAAAAAAAAAAAAAALELUYA; ")
            break
        inmates = boxes_required[inmates - 1][1] #AAAAAAAAAALELUYA MEJORAR
        print(inmates, "-------------")
        x = x + 1
        if x > 50:
            break    


if l == 100:
    win_or_loose = 1
else:
    win_or_loose = 0

