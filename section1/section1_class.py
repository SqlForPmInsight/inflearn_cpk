class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print("저는", self.name, "입니다.")

p = Person("파이썬")
p.say_name() 