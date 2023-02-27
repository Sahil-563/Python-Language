x=1
while x != 4:
    
    print("hi")
    x+=1


           
           #Use of break statemetn in while loop:---

i=1
while i<4:
    num=int(input("Enter a number"))
    if num == 0:
        print("Program exited()")
        break
    sq=num*num
    int(sq)
    
    print(f"The square of {num} is {sq}")
    i+=1
else:
    print("done")
    

             #use of continue statement in while loop:---
i=1
while i<4:
    if i==2:
        i+=1
        continue
        
    print(i)
    i+=1
    