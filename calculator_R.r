### R calculator - Functions
### Nicolenco Svetlana
### 10265376

?Math

#1. sum(x) computes the sum of the elements of a REAL or LOGICAL vector x.
add = function(x,y) sum(x,y)

#2. arithmetic function - substraction
substract = function(x,y) x-y

#3. arithmetic function - multiplication
multiply <- function(x, y) x * y

#4. arithmetic function - division
divide <- function(x, y) {
  if (y == 0) {
    return ("zero division error")
  } else {
    return(x / y)
  }
}

#5. sqrt(x) returns the square roots of the elements of x, when x is a REAL scalar, vector, matrix or array.
square = function(x) sqrt(x)

#6. exp(x) returns the exponential function (e^x) of the elements of x, when x is a REAL scalar, vector, matrix or array.
exp = function(x) exp(x)

#7. log(x) returns the natural logarithm (base e log) of the elements of x, when x is a REAL scalar, vector, matrix or array.
log <- function(x) log(x)

#8. cos(x) computes the cosine of the values of the elements of x, where x is a REAL scalar, vector, matrix or array.
# The argument is considered to be in units of radians, degrees or cycles as determined by the value of option 'angles'.  The default is radians.
cos <- function(x) cos(x)

#9. TRUNC(x) truncates the number x to an integer by removing the fractional part of x.trunc(5.99) is 5
trunc = function(x) trunc(x)

#10.	floor(3.580) is 3
floor = function(x) floor(x)


print("Select operation.")
print ("1: ADDITION")
print ("2: SUBTRACTION")
print ("3: MULTIPLICATION")
print ("4: DIVISION")
print ("5: SQROOT")
print ("6: EXPONENT")
print ("7: NAT_LOG")
print ("8: COS")
print ("9: TRUNCATE")
print ("10: FLOOR")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))
                 
x = as.integer(readline(prompt="Enter first number: "))
y = as.integer(readline(prompt="Enter second number: "))                 
                 
result = switch(choice, add(x,y), substract(x,y), multiply(x,y), divide(x,y), square(x), exp(x), log(x), cos(x), trunc(x), floor(x))

print(result)


