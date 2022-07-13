import random as rd

def inmates_scape_probability():
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
                break
            inmates = boxes_required[inmates - 1][1] 
            x = x + 1
            if x > 50:
                break    

    if l == 100:
        win_or_loose = 1
    else:
        win_or_loose = 0
        
    return win_or_loose


prob_lst = []
for i in range(1000000): 
    result = inmates_scape_probability()
    prob_lst.append(result)
    print(i)
   
a = sum(prob_lst)

print(a/1000000)
