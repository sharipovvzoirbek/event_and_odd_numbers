#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 7640
#Create a variable "sum_even" and assign it 0.
a=var_int//1000
b=var_int//100%10
c=var_int//10%10
d=var_int%10


a = (a-1)%2
b = (b-1)%2
c = (c-1)%2
d = (d-1)%2
print(a+b+c+d)
#Find the sum of the even digits in the variable "var_int".
