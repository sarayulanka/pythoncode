# regular function without lambda
def addfive(a):
    return a + 5


print(addfive(6))

# regular function with lambda
# lambdavar =  lambda arguments : expression
add5 = lambda x: x + 5

print(add5(6))

addnum = lambda x, y: x + y

sum = addnum(5, 6)
print(sum)

multiplynum = lambda num, mf: num * mf

product = multiplynum(5, 6)
print(product)

# value_if_true if (condition) else value_if_false

even_odd = lambda num: "even"if num % 2 == 0 else "odd"
print(even_odd(6))

name = lambda firstname, lastname: firstname + " " + lastname if lastname.lower() == "taylor" else firstname
print(name("taylor", "swift"))
print(name("swift", "Taylor"))
