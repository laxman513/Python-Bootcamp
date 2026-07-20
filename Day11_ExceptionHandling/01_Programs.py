"""
==========================================
Day 11 - Exception Handling
Programs 1-15
==========================================
"""

# -----------------------------------------
# Program 1
# -----------------------------------------

print("Program 1")
print("-" * 30)

print(10 / 2)

# -----------------------------------------
# Program 2
# -----------------------------------------

print("\nProgram 2")
print("-" * 30)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------------------
# Program 3
# -----------------------------------------

print("\nProgram 3")
print("-" * 30)

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Invalid Index")

# -----------------------------------------
# Program 4
# -----------------------------------------

print("\nProgram 4")
print("-" * 30)

try:
    print(100 / 20)
except ZeroDivisionError:
    print("Error")

# -----------------------------------------
# Program 5
# -----------------------------------------

print("\nProgram 5")
print("-" * 30)

try:
    print(int("100"))
except ValueError:
    print("Invalid Number")

# -----------------------------------------
# Program 6
# -----------------------------------------

print("\nProgram 6")
print("-" * 30)

try:
    print(int("abc"))
except ValueError:
    print("Please enter a valid integer.")

# -----------------------------------------
# Program 7
# -----------------------------------------

print("\nProgram 7")
print("-" * 30)

try:
    value = int(input("Enter a Number: "))
    print("You Entered:", value)
except ValueError:
    print("Invalid Input")

# -----------------------------------------
# Program 8
# -----------------------------------------

print("\nProgram 8")
print("-" * 30)

try:
    number = int(input("Enter Number: "))
    print(100 / number)
except ZeroDivisionError:
    print("Number cannot be zero.")
except ValueError:
    print("Please enter only numbers.")

# -----------------------------------------
# Program 9
# -----------------------------------------

print("\nProgram 9")
print("-" * 30)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Divide by Zero")
except ValueError:
    print("Value Error")

# -----------------------------------------
# Program 10
# -----------------------------------------

print("\nProgram 10")
print("-" * 30)

try:
    print(int("abc"))
except ValueError:
    print("Invalid Number")
except Exception as e:
    print(e)

# -----------------------------------------
# Program 11
# -----------------------------------------

print("\nProgram 11")
print("-" * 30)

try:
    print(10 / 2)
except Exception:
    print("Error")

# -----------------------------------------
# Program 12
# -----------------------------------------

print("\nProgram 12")
print("-" * 30)

try:
    print(10 / 0)
except Exception as e:
    print(e)

# -----------------------------------------
# Program 13
# -----------------------------------------

print("\nProgram 13")
print("-" * 30)

try:
    numbers = [10]
    print(numbers[5])
except Exception as e:
    print(type(e))

# -----------------------------------------
# Program 14
# -----------------------------------------

print("\nProgram 14")
print("-" * 30)

try:
    print(int("50"))
except Exception:
    print("Error")

print("Completed")

# -----------------------------------------
# Program 15
# -----------------------------------------

print("\nProgram 15")
print("-" * 30)

try:
    print(100 / 10)
except ZeroDivisionError:
    print("Error")
else:
    print("Division Successful")

# -----------------------------------------
# Program 16
# -----------------------------------------

print("\nProgram 16")
print("-" * 30)

try:
    print(100 / 0)
except ZeroDivisionError:
    print("Divide Error")
else:
    print("Success")

# -----------------------------------------
# Program 17
# -----------------------------------------

print("\nProgram 17")
print("-" * 30)

try:
    print(int("50"))
except ValueError:
    print("Invalid")
else:
    print("Completed Successfully")

# -----------------------------------------
# Program 18
# -----------------------------------------

print("\nProgram 18")
print("-" * 30)

try:
    print(int("abc"))
except ValueError:
    print("Invalid Number")
finally:
    print("Finally Block Executed")

# -----------------------------------------
# Program 19
# -----------------------------------------

print("\nProgram 19")
print("-" * 30)

try:
    print(10 / 2)
finally:
    print("Program Finished")

# -----------------------------------------
# Program 20
# -----------------------------------------

print("\nProgram 20")
print("-" * 30)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Handled")
finally:
    print("Cleanup Completed")

# -----------------------------------------
# Program 21
# -----------------------------------------

print("\nProgram 21")
print("-" * 30)

try:
    raise ValueError("Invalid Input")
except ValueError as e:
    print(e)

# -----------------------------------------
# Program 22
# -----------------------------------------

print("\nProgram 22")
print("-" * 30)

age = 20

try:
    if age >= 18:
        print("Eligible")
    else:
        raise ValueError("Not Eligible")
except ValueError as e:
    print(e)

# -----------------------------------------
# Program 23
# -----------------------------------------

print("\nProgram 23")
print("-" * 30)

age = -1

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)

# -----------------------------------------
# Program 24
# -----------------------------------------

print("\nProgram 24")
print("-" * 30)

class MyError(Exception):
    pass

try:
    raise MyError("Custom Exception Raised")
except MyError as e:
    print(e)

# -----------------------------------------
# Program 25
# -----------------------------------------

print("\nProgram 25")
print("-" * 30)

try:
    raise ValueError("Wrong Value")
except ValueError:
    print("Handled Successfully")

# -----------------------------------------
# Program 26
# -----------------------------------------

print("\nProgram 26")
print("-" * 30)

try:
    file = open("sample.txt")
except FileNotFoundError:
    print("File Not Found")

# -----------------------------------------
# Program 27
# -----------------------------------------

print("\nProgram 27")
print("-" * 30)

try:
    data = {"name": "Laxman"}
    print(data["age"])
except KeyError:
    print("Key Not Found")

# -----------------------------------------
# Program 28
# -----------------------------------------

print("\nProgram 28")
print("-" * 30)

try:
    print("Hello" + 10)
except TypeError:
    print("Type Mismatch")

# -----------------------------------------
# Program 29
# -----------------------------------------

print("\nProgram 29")
print("-" * 30)

try:
    import math
    print(math.sqrt(144))
except Exception as e:
    print(e)

# -----------------------------------------
# Program 30
# -----------------------------------------

print("\nProgram 30")
print("-" * 30)

try:
    x = 10
    y = 5
    print(x + y)
except Exception:
    print("Error")
else:
    print("Addition Successful")
finally:
    print("Program Ended")

# -----------------------------------------
# Program 31
# -----------------------------------------

print("\nProgram 31")
print("-" * 30)

try:
    number = int(input("Enter Number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------------------
# Program 32
# -----------------------------------------

print("\nProgram 32")
print("-" * 30)

try:
    names = ["Ram", "Shyam", "Mohan"]
    print(names[10])
except IndexError as e:
    print(e)

# -----------------------------------------
# Program 33
# -----------------------------------------

print("\nProgram 33")
print("-" * 30)

try:
    employee = {
        "id": 101,
        "name": "Laxman"
    }

    print(employee["salary"])

except KeyError as e:
    print(e)

# -----------------------------------------
# Program 34
# -----------------------------------------

print("\nProgram 34")
print("-" * 30)

try:
    result = 10 + "20"
except TypeError as e:
    print(e)

# -----------------------------------------
# Program 35
# -----------------------------------------

print("\nProgram 35")
print("-" * 30)

try:
    file = open("employee.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("employee.txt does not exist.")

# -----------------------------------------
# Program 36
# -----------------------------------------

print("\nProgram 36")
print("-" * 30)

try:
    age = int(input("Enter Age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as e:
    print(e)

# -----------------------------------------
# Program 37
# -----------------------------------------

print("\nProgram 37")
print("-" * 30)

class InvalidSalaryError(Exception):
    pass

try:
    salary = -5000

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

except InvalidSalaryError as e:
    print(e)

# -----------------------------------------
# Program 38
# -----------------------------------------

print("\nProgram 38")
print("-" * 30)

try:
    print("Inside Try")
except:
    print("Inside Except")
else:
    print("Inside Else")
finally:
    print("Inside Finally")

# -----------------------------------------
# Program 39
# -----------------------------------------

print("\nProgram 39")
print("-" * 30)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Handled")
finally:
    print("Execution Completed")

# -----------------------------------------
# Program 40
# -----------------------------------------

print("\nProgram 40")
print("-" * 30)

try:
    print(int(input("Enter Number: ")))
except Exception as e:
    print(type(e))
    print(e)

# -----------------------------------------
# Program 41
# -----------------------------------------

print("\nProgram 41")
print("-" * 30)

try:
    numbers = [10, 20, 30]
    print(numbers[1])
except Exception:
    print("Error")
else:
    print("Index Access Successful")

# -----------------------------------------
# Program 42
# -----------------------------------------

print("\nProgram 42")
print("-" * 30)

try:
    x = 100
    y = 25

    print(x / y)

except Exception:
    print("Error")

finally:
    print("Division Completed")

# -----------------------------------------
# Program 43
# -----------------------------------------

print("\nProgram 43")
print("-" * 30)

try:
    raise RuntimeError("Something went wrong.")
except RuntimeError as e:
    print(e)

# -----------------------------------------
# Program 44
# -----------------------------------------

print("\nProgram 44")
print("-" * 30)

try:
    value = int("25")
    print(value)
except Exception:
    print("Error")
else:
    print("Conversion Successful")
finally:
    print("Program Finished")

# -----------------------------------------
# Program 45
# -----------------------------------------

print("\nProgram 45")
print("-" * 30)

try:
    print("Python Exception Handling Completed Successfully.")
except Exception:
    print("Error")

# -----------------------------------------
# Program 46
# -----------------------------------------

print("\nProgram 46")
print("-" * 30)

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print("Result:", x / y)
except ValueError:
    print("Please enter only integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# -----------------------------------------
# Program 47
# -----------------------------------------

print("\nProgram 47")
print("-" * 30)

try:
    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("Marks:", marks)

except ValueError as e:
    print(e)

# -----------------------------------------
# Program 48
# -----------------------------------------

print("\nProgram 48")
print("-" * 30)

class InvalidPINError(Exception):
    pass

try:
    pin = "123"

    if len(pin) != 4:
        raise InvalidPINError("PIN must contain exactly 4 digits.")

except InvalidPINError as e:
    print(e)

# -----------------------------------------
# Program 49
# -----------------------------------------

print("\nProgram 49")
print("-" * 30)

try:
    names = ["Ram", "Shyam"]
    print(names[0])
except Exception:
    print("Error")
else:
    print("First element accessed successfully.")

# -----------------------------------------
# Program 50
# -----------------------------------------

print("\nProgram 50")
print("-" * 30)

try:
    print("Opening Database Connection")
finally:
    print("Closing Database Connection")

# -----------------------------------------
# Program 51
# -----------------------------------------

print("\nProgram 51")
print("-" * 30)

try:
    number = int("500")
    print(number)
except Exception:
    print("Error")
finally:
    print("Conversion Completed")

# -----------------------------------------
# Program 52
# -----------------------------------------

print("\nProgram 52")
print("-" * 30)

try:
    print(50 / 5)
except Exception:
    print("Error")
else:
    print("Division Successful")
finally:
    print("Program Finished")

# -----------------------------------------
# Program 53
# -----------------------------------------

print("\nProgram 53")
print("-" * 30)

try:
    print(50 / 0)
except ZeroDivisionError as e:
    print(type(e))
    print(e)

# -----------------------------------------
# Program 54
# -----------------------------------------

print("\nProgram 54")
print("-" * 30)

try:
    employee = {"id": 101}
    print(employee["salary"])
except KeyError as e:
    print("Missing Key:", e)

# -----------------------------------------
# Program 55
# -----------------------------------------

print("\nProgram 55")
print("-" * 30)

try:
    raise RuntimeError("Runtime Error Example")
except RuntimeError as e:
    print(e)

# -----------------------------------------
# Program 56
# -----------------------------------------

print("\nProgram 56")
print("-" * 30)

try:
    print(int("Python"))
except ValueError:
    print("String cannot be converted into integer.")

# -----------------------------------------
# Program 57
# -----------------------------------------

print("\nProgram 57")
print("-" * 30)

try:
    numbers = [100, 200, 300]
    print(numbers[10])
except IndexError:
    print("Invalid List Index")

# -----------------------------------------
# Program 58
# -----------------------------------------

print("\nProgram 58")
print("-" * 30)

try:
    file = open("abc.txt")
except FileNotFoundError:
    print("abc.txt not found.")

# -----------------------------------------
# Program 59
# -----------------------------------------

print("\nProgram 59")
print("-" * 30)

try:
    raise Exception("General Exception")
except Exception as e:
    print(e)

# -----------------------------------------
# Program 60
# -----------------------------------------

print("\nProgram 60")
print("-" * 30)

print("Congratulations!")
print("You have completed Day 11 - Exception Handling.")