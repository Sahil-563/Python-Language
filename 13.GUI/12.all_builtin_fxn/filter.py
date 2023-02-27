#filter() function is used to filter a list by applying a defined function to calculate even number by a function

lst=[1,3,2,4,7,6,8,9]
def evencheck(num):
    if num%2==0:
        return True
    else:
        return False

lst2=filter(evencheck,lst)
even_lst=[]
for ele in lst2:
    even_lst.append(ele)
print(even_lst)   #filtered list of even numbers
