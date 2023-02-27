num=123
r_no=0
while num!=0:
    lst_digit=num%10
    r_no=r_no*10+lst_digit
    num//=10

print(r_no)



    