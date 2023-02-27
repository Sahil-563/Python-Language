                  #tuples are immutible (can't be changed) 
tuple=(1,2,3)    #tuples are identified by square brackets
print(tuple)
tp=(1,)  #if there is only one value in tuple then add a comma with it to identify it
print(tp)
tp=("sahil","sahil thakur","vishal")
#tp[1]="yo"   #the value can't be changed because tuple is immutible
print(tp)
x=["22","sahil"]   #list
x[1]=32
print(x)


#tp1=tuple("13")

#tp2=tuple("123456789")

#print(tp)
#print(tp2)

                     
                        #tuple slicig
#you can acess the elements of a tuple by indexing but you can't del modify them
#print(tp1[1])
#you can add elements to a tuple as
#tp3=tp1+tuple("akshita")
#print(tp3)

           #TO MODIFY TUPPLE ELEMENTS
tp1=(1,2,4,5,6,7)
lst=list(tp1)
lst.remove(4)
tp1=tuple(lst)
print(tp1) 
         
         #EMBEDDED TUPLE
tpl1=(1,2,3,4,5,6)
tpl2=(7,8,9,10)
tpl=[tpl1 , tpl2]  #niow this is a list in which we can do indexig and can modify or change elements
tpl[1]=1
print(tpl)
             
        #UNPACKING OF TUPLES
tpl=(*tpl1,*tpl2)
print(tpl)
tp4=("sahil","vishal")
print(tp4)
x= tuple('sahil')
print(x)