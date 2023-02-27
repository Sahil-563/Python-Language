         #all() fum=nction is used to print true for true value and false for fals value

              #For lists:---

lst = [1,2,3,4]  #In this list all the values are true that's why the print statement returned true
print(all(lst))
lst1 = [1,2,3,0]   #In this list all the values are not true that's why the print statement returned false
print(all(lst1))
lst2 = [1,2,3,"0"]  #In this case the print statement will return true since it has a string and all true values in it
print(all(lst2))
lst3 = []        #Empty list also returns true since it was Null as its value not zero 
print(all(lst3))

                     #For strings:--      
x = "Sahil"  #In this is case it again returns true
print(all(x))
          
          #FOR DICTIONARIES:--
dict = {}    
print(all(dict))  # For empty dictionary all function always returns True since it has null value
dict2 = {1:0,2:0} 
print(all(dict2))    #If a dictionary has 0 as it's values then it returns True
dict3 = {0:1,0:2}   
print(all(dict3))    #If a dictionary has 0 as it's keys then it returns False


       # For Tuple:---
tpl = (1,0)  
print(all(tpl))   #It will returns false since it has a false value in it
        
        #For sets:--
st = {1,2,3,0}
print(all(st))

