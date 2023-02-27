for e in "pyhton":
    print(e)

for x in [1,2,3]:
    print(x)

x=[1,2,3]
for x in x:
    print(x)


lst=["python","Java","C++",45,"JS"]
for ele in lst:
    if ele==45:
        continue
    y=ele.lower()
    print(y)

               #Having unique list from a buzzed list:--
lst=[12,34,3,2,1,345,3121,4,5,6,7,4,4,4,6,5,4]
unique_lst=[]
for num in lst:
    if num in unique_lst:
        continue
    unique_lst.append(num)
unique_lst.sort()
print(unique_lst)     
                        #or

lst=[12,34,3,2,1,345,3121,4,5,6,7,4,4,4,6,5,4]
unique_lst=set(lst)
unique_lst=list(unique_lst)
print(unique_lst)


tpl=(1,"sahil",2)
for ele in tpl:
    print(ele)