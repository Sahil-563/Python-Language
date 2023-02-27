#compile,exec(),eval()
code = 'print(sum([1,2,3]))'
y= compile(code,filename = "z",mode="eval")
eval(code)

