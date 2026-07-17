print(True + True)
print(True + False)
print(False * 10)

print(type(True))
print(type(False))

print(int(True))
print(int(False))

print(isinstance(False, int))

print(isinstance(True, int))

print(False == 0)

results = [True, False, False, True, True]

count = 0
for r in results:
    if r:
        count += 1
print(f"count: {count}")
print(f"Sum is: {sum(results)}")