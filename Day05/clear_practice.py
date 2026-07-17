numbers = [10, 20, 30]
numbers.clear()
print(numbers)

students = ["ram", "Shyam", "Krishna"]
students.clear()
print(len(students))

colour = ["Red", "Green"]
colour.clear();
colour.append("Blue")
print(colour)

cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai"]
print("Original cities:", cities)

cities.clear()
print("Afterclear cities:", cities)
print("Length of cities:", len(cities))

cities.append("Bangalore")
print("Update cities:", cities)
