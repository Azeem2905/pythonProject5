def greeting(first,last):
    greeting = f"Hello,{first} {last} Congrats For Creating Name Generator"
    return greeting

first=input("Enter First Name: ")
last=input("Enter Last Name: ")

ggreeting = greeting(first,last)
print(ggreeting)