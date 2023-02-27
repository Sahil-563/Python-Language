#map:--
lst = ["red",'yellow','green']
def upper(col):
    return col.upper()
print([col for col in map(upper,lst)])