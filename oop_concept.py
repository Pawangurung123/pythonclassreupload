# class Myclass:
#     x=5

# p1=Myclass()
# print(p1.x)
# print(p1)

# class Person:
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age

# p1=Person("John", 36)

# print(p1.name)
# print(p1.age)

"""
1.Class and object
2.Inheritance
3.Encapsulation
4.Polymorphism
5.Abstraction
6.Accessor and mutator function( Getter ad Starter)
7.Access modifier (public, private, protected)
"""
#1. Class and object
    #-> noun 
# state (charactristics, property)
    #-> adjective
#-> behaviour (action, function)
    #-> verb

#Car,
    #color, model, manuf_year
    #start, stop, run

# class Laptop:
#     def __init__(self, brand, color, ram="2gb"):
#         #It is called instance variable (object ko variable vakole)
#         self.brand= brand
#         self.color= color
#         self.ram= ram

#     #called Instance method because object is used.
#     def reboot(self):
#         print(f"{self.brand} Laptop is rebooting.")

# lenovo =Laptop("lenevo", "Black", "16gb")
# print(lenovo.ram)

# dell= Laptop("dell", "red")
# print(dell.ram) #cpassing default value from class

# lenovo.reboot()
# dell.reboot()




# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1= num1
#         self.num2=num2

#     def sum(self):
#         print(f"sum is {self.num1+self.num2}")

#     def difference(self):
#         print(f"difference is {self.num1-self.num2}")

#     def product(self):
#         print(f"product is {self.num1*self.num2}")

#     @staticmethod #when u dont wanna use object use this decorator.
#     def square_root(num):
#         print(f"square root is {num**0.5}")

# c=Calculator(5,7) #This is an object
# # print(c.__dict__)
# # c.sum()
# # c.difference()
# # c.product()
# c.square_root(4)
# Calculator.square_root(4) #can call with class too not only object



    
# class Student:

#     #class or static variable #can be created if common and used for every object 
#     college_name="Annapurna College"

#     def __init__(self, _id , name, address):
#         self._id =_id
#         self.name = name
#         self.address= address

# s=Student("001", "Ram", "KTM")
# # print(s._id, s.name, s.address)
# # print(s.college_name)
# #print(s.__dict__) #only represents instance variable not class variable

# st=Student("002", "Shyam", "PKR")
# # print(st.college_name)
# #print(st.__dict__)
# print(Student.college_name) #can call class variable directly through class name.


# class Product:

#     def __init__(self, name, price):
#         self.name= name 
#         self.__price= price #double underscore infront variable makes it private #Name mangaling

#     @property 
#     def price(self):             #acceser getter
#         return self.__price
    
#     @price.setter
#     def price(self, price):            #mutator setter
#         if price > 0:
#             self.__price= price 


#     # def get_price(self):
#     #     return self.__price

#     # def set_price(self, price):
#     #     if price>0:
#     #         self.__price= price 

# p=Product("Pant", 1600)
# print("Intial value", p.price)
# p.price=0
# print("final value", p.price)



class Product:

    shop_name= "ABC SHOP"

    def __init__(self, name, price):
        self.__name=name
        self.price=price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # if name > 0:
            self. __name= name

    def __str__(self):
        return f"{self.name} => {self.price}"

    def __eq__(self, obj):    #operator overloading
        return self.price== obj.price


p=Product("Pant", 1600)
# c=Product("Tshirt", 1600)
# print(p==c) #operation overloading 
print(dir(str))
# print("Initial value", p.name)
# p.name="shorts"
# print("final value", p.name)
# print(p)

        