class Student:
    def __init__(self, name, age, goal):
        self.name = name
        self.age = age
        self.goal = goal

    def introduce(self):
        print(f"Hi, I'm {self.name}.")
        print(f"I'm {self.age} years old.")
        print(f"My goal: {self.goal}")

    def __str__(self):
        return f"Student({self.name})"

me = Student("Alok Vishwakarma", 21, "GenAI Developer")
me.introduce()
print(me)