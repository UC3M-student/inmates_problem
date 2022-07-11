import random as rd

inmates = rd.sample(range(1,101,1),100)
boxes = rd.sample(range(1,101,1),100)

boxes_required = [(inmates[i-1],boxes[i-1]) for i in range(100)]
