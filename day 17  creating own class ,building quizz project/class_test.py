class Test:
    def __init__(self, id , name , age):
        self.id = id
        self.name = name
        self.age = age

    def increase_age(self, emp):
        emp.age += 5
        self.age += 4