#Implement a recursive function to calculate the factorial of a given number.
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
number=int(input("enter the number:") )
res= factorial(number)
print("the factorial of {} is {}".format(number,res))