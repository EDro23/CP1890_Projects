def fun_gen():
    yield "CP1890 Class is terrible"
    yield "Maybe its because of the instructor"
    yield "Or is it the students? Putting in the points"

objt = fun_gen()

print(type(objt))
print(next(objt))
print(next(objt))
print(next(objt))


test_list = [1,4,5,6,7]
def print_even(some_list):
    for i in some_list:
        if i%2 == 0:
            yield i


print("The even numbers in my list are: ", end=' ')
for k in print_even(test_list):
    print(k, end=' ')