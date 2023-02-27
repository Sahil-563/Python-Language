    #printing a lst which is sorted and donot have duplicate elements

lst=[1,3,2,45,3,1,2,5,66,7,4]
def rm_dp(l):
    unique_lst=list(set(l))
    unique_lst.sort()
    return unique_lst
print(lst)      #here we print the actual list
print(rm_dp(lst))  #here we print the sorted list in which the duplicate elements are removed

