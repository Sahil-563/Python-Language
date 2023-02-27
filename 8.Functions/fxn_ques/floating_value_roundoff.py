def round_off(*l):
    sum=0
    d=[]
    for ele in l:
        sum+=ele
        value=str(ele).split(".")
        #print(value)
        d.append(len(value[1]))
    min_d=min(d)
    return (round(sum,min_d))

        
   

print(round_off(1.25,1.3))