import random as rd

inmates = range(1,101,1)
boxes = rd.sample(range(1,101,1),100)

boxes_required = [(inmates[i],boxes[i-1]) for i in range(100)]

#print(boxes_required[(boxes_required[7][1])][1] , "ALELUYAAAA")

print(boxes_required)

l = 0
y = 0
for i in inmates:
    x = 0
    y = y + 1
    #print(i)
    #try:
    #if i == boxes_required[i - 1][1]:
    #l = l + 1
    #print("--------------------------------------")
    #except:
    #x = x + 1
    
    print(i)
    
    try:
        inmates = boxes_required[((boxes_required[i -1][1])-1)][1] # PERFECT ; inmates = boxes_required[((boxes_required[i -1][1])-1)][1]
    except:
        continue
    #print(inmates, " INMATES HAS BEEN PRINTED")
    #print(inmates, "INMATES")
    
    while x < 5:
        if i == inmates:
            x = 51
            l = l + 1
            break
        inmates = boxes_required[inmates - 1][1] #AAAAAAAAAALELUYA

        #inmates = boxes_required[inmates - 1][1]
        print(inmates, "-------------")

        #print("x is equal to: ", x)
        #print("x is equal to : ", x)
        x = x + 1
        #if i == inmates:
            #print(inmates, " this inmate has found his number ")
            #x = 51
            #l = l + 1
            #print(l, "-------------------------------------------------")
            #print(l, "lllllllllllllllll")
        if x > 50:
            #print("break")
            break    

#print(l, "if is 100 you all are free")

if l == 100:
    win_or_loose = 1
 
 
print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY -> ", y)
#print(l)


    
    
    
