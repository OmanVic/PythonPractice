# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(5, 6, 7))

def calculate(n, **kwargs):
    # for here, there in kwargs.items():
    #     print(here)
    #     print(there)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=4)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="nissan")
print(my_car.model)