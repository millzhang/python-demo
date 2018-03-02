class Dog():  #类
    def __init__(self, name, age):  #构造方法
        ## 形参self必不可少，而对应的实参会自动传递，不需要手动传递
        self.name = name
        self.age = age
        self.legs = 4 #给属性指定默认值

    def sit(self):  #方法
        print(self.name.title() + " is going to sit")

    def roll_over(self):  #方法
        print(self.name.title() + " rolled over")

    def getLegs(self):
        return str(self.legs)

# 创建类的实例

dog = Dog('key',25)
dog.sit()
dog.roll_over()
print(dog.name)
print(dog.getLegs())
# 修改属性值
dog.legs = 10
print(dog.getLegs())

# 子类

class LittleDog(Dog): # 继承与Dog父类
    def __init__(self,name,age):
        super().__init__(name,age)

    #子类自定义方法
    def getAge(self):
        return str(self.age)

    #重写父类方法
    def getLegs(self):
        return str(3)

little_dog = LittleDog('smallpipi',2)
print('Little:'+little_dog.name)
print('Little:'+little_dog.getLegs())
print('Little:'+little_dog.getAge())
#print(dog.getAge())  # ERROR:AttributeError: 'Dog' object has no attribute 'getAge'
