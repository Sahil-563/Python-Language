#Write a Program to Convert Binary Number to Decimal manually by creating user-defined function

def binary_no(binary_no):
    decimal_no=0
    i=0
    while binary_no != 0:
        lst_digit=binary_no%10
        decimal_no+=lst_digit*pow(2,i)
        i+=1
        binary_no//=10
       
    return decimal_no
bin_no=int(input("Enter a number: "))
print(f"The Decimal form of {bin_no} is: {binary_no(bin_no)}")

