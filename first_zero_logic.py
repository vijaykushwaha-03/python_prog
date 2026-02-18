lst = [1,0,0,2,3,0,4,0,5,0]
emt = []
fill = []

for i in lst:
    if i == 0:
        emt.append(i)
    else:
        fill.append(i)
    
print(emt+fill)