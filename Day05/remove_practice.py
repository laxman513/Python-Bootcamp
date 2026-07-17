fruits = ["Apple", "Banana", "Orange", "Manmgo", "Banana"]
print("original fruits:", fruits)

fruits.remove("Banana")
print("After Bana removed:", fruits)

if "Grapes" in fruits:
    fruits.remove("Grapes")
else:
    print("Grapes not found")

print("Final fruits:", fruits)

numbers = [10, 20]

x = numbers.remove(20)

print(x)
print(numbers)