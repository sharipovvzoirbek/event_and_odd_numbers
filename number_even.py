#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 4444
#Print the number of even digits in the variable "var_int".
a=var_int//1000
b=var_int//100%10
c=var_int//10%10
d=var_int%10


a = (a-1)%2
b = (b-1)%2
c = (c-1)%2
d = (d-1)%2
print(a+b+c+d)