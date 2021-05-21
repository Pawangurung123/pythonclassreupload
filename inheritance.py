#child class "IS A" parent class or #sublass "IS A " superclass 
# "iS A " relation should be fulfilled so inherit will succeed

# class Person:

#     def __init__(self, name, address, contact):
#         self.name= name
#         self.address= address
#         self.contact= contact 

#     def walk(self):
#         print(f"{self.name} is walking")
    
# class Student(Person): #syntax of inheriting person in student #student = child or sub class
#         #Person is parent or superclass

#     def __init__(self, name ,address, contact):
#          super(). __init__(name, address, contact)     
 
# class Teacher(Person):
#     def __init__(self, name, address, contact):
#         super().__init__(name, address, contact)


# s= Student("ram", "Ktm", "9818")      
# print(s.__dict__)                          
# s.walk()

# t=Teacher("hari", "mandktr", "0123")
# t.walk()




class Bird:

    def __init__(self, name) -> None:
        self.name=name

    def fly(self):
        print(f"{self.name} is flying")  #overiding 

class Pigeon(Bird):
    def __init__(self, name):
        super().__init__(name)

class Ostrich(Bird): 
    def __init__(self, name):
        super(). __init__(name)

    def fly(self):
        print(f"{self.name} couldn't fly")

class Hummingbird(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)

    def fly(self):
        super().fly()
        print("It also can fly backwards")
    


p=Pigeon("Pidori")
p.fly()
o=Ostrich("Mustang")
o.fly()
h=Hummingbird("Tiny")
h.fly()


"""Note """
#we get polymorphism by using operating overloading and operator overriding
#Polymorphism means same thing showing different form or behaviour like .fly() in above example