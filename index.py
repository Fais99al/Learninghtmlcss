def factorial1(n):
    temp=1
    for i in range(2,n+1):
      temp=temp*i
    return temp
print(factorial1(5))