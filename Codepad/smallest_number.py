a=[1,2,3,4]
x=a[0]
for i in range(len(a)):
    if a[i]<x:
        x=a[i]
print(x)

def smallest_number(arr):
    small=arr[0]
    for i in range(len(arr)):
        if arr[i]<small:
            small=arr[i]
    return small
small_number=[1,2,3,4]
result=smallest_number(small_number)
print("smallest number:",small_number)