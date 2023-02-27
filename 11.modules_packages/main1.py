import module1    #importing a module
module1.greetuser("Sahil")
from module1 import greetuser  #importing a specific function from a module1
greetuser("Arpit")
from module1 import *  #By this star (*) all the functions of module1 are imported
wish("Akshita")
from module1 import greetuser as gt  #this is called alicing
gt("Rituraj")
import module1 as mod #this is also aliacing
     

     #importing a package
import package1
from package1 import module1
from package1.module2 import sus #importing specific function from a specific module stored in package1 
sus("Adarsh")
from package1 import module1
from module1 import greetuser
greetuser("aman")