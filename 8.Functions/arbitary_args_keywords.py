#Here user passes a dictionary in short because user passes a key value pair like:-- "name":"sahil"  
  
def info(**kw):
    for k,v in kw.items():      #we have to use a builtin fxn items 
        print(k,":",v)
info(name="Sahil",Marks=44,Age=19)    #here name is key and "sahil" is value

            