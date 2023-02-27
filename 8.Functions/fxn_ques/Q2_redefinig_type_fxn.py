#redefinig type fxn:--
def type_fxn(data):
    dt=str(type(data))
    if "str" in dt:
        print("String")
    elif "int" in dt:
        print("Integer")
    elif "float" in dt:
        print("Float")
    elif "complex" in dt:
        print("Complex")
    
type_fxn(3)
    


