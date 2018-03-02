def greet(name, age):
    print('Hello ' + name + ',you are ' + str(age) + ' years old this year!')


greet('HanMeimei', 2)
greet(age="12", name="LiLei")


def makePizza(*toppings):
    print(toppings)


makePizza('mushrroms', 'greenpapers')


def makeFood(**foods):
    print(foods.items())


makeFood(name="orange", color="red", taste="good")