try:
    num1=int(input("Enter any number:"))
    num2=int(input("Enter another number:"))
    
    # print(n)
except ValueError:
    print("Input must be number for operation")
except NameError as err :
    print(err)

else:
    print(f"Sum of {num1} and {num2} is {num1+num2}.")

finally:
    print("Completed")

    
name=input("Enter your name:")
print(f"Your name is {name}.")
print("Program Completed")

#exceptional handeling
#structure should be in order like below:
#except can be multiple, else and finally is optional

try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

