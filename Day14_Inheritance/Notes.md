# Day 14 — Python OOP: Inheritance, super(), Multiple Inheritance and MRO

---

## 1. Day 14 Overview

Day 14 focuses on advanced Object-Oriented Programming concepts in Python.

Topics:
1. Inheritance
2. Parent and child classes
3. Single inheritance
4. Multilevel inheritance
5. Hierarchical inheritance
6. Multiple inheritance
7. Method overriding
8. Calling parent methods
9. `super()`
10. Constructor inheritance
11. Constructor chaining
12. Multiple inheritance and MRO
13. Diamond inheritance
14. C3 Linearization
15. `isinstance()`
16. `issubclass()`
17. Common mistakes
18. Python vs Java inheritance

---

## 2. What is Inheritance?

Inheritance allows one class to reuse properties and methods of another class.

The class providing functionality is the **parent/base/superclass**.

The class receiving functionality is the **child/derived/subclass**.

```python
class Person:

    def display_name(self):
        print("Person")


class Student(Person):
    pass


student = Student()
student.display_name()
```

Output:

```text
Person
```

`Student` inherits `display_name()` from `Person`.

---

## 3. Parent and Child Classes

```python
class Person:

    def display_name(self):
        print("Person")


class Student(Person):

    def study(self):
        print("Studying")
```

`Person` is the parent.

`Student` is the child.

```text
Person
   |
   v
Student
```

---

## 4. Why Do We Need Inheritance?

### 4.1 Code Reusability

Common functionality can be written once in the parent.

```python
class Person:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Student(Person):
    pass


class Employee(Person):
    pass
```

Both `Student` and `Employee` can use `eat()` and `sleep()`.

### 4.2 Code Maintenance

Common functionality can be maintained in one parent class.

### 4.3 Extensibility

A child can add its own methods.

```python
class Student(Person):

    def study(self):
        print("Studying")
```

### 4.4 Method Overriding

A child can provide its own implementation of an inherited method.

---

## 5. Basic Inheritance Syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

Example:

```python
class Person:

    def show(self):
        print("Person")


class Student(Person):
    pass
```

`Student(Person)` means Student inherits from Person.

---

## 6. Types of Inheritance

Common types:

1. Single inheritance
2. Multilevel inheritance
3. Hierarchical inheritance
4. Multiple inheritance
5. Hybrid inheritance
6. Diamond inheritance

---

## 7. Single Inheritance

One child inherits from one parent.

```text
Parent
   |
   v
Child
```

Example:

```python
class Person:

    def show(self):
        print("Person")


class Student(Person):

    def study(self):
        print("Studying")


student = Student()

student.show()
student.study()
```

Output:

```text
Person
Studying
```

---

## 8. Multilevel Inheritance

Inheritance happens through multiple levels.

```text
Grandparent
     |
     v
  Parent
     |
     v
  Child
```

Example:

```python
class Person:

    def person_info(self):
        print("Person")


class Employee(Person):

    def employee_info(self):
        print("Employee")


class Manager(Employee):

    def manager_info(self):
        print("Manager")


manager = Manager()

manager.person_info()
manager.employee_info()
manager.manager_info()
```

Output:

```text
Person
Employee
Manager
```

Manager inherits from Employee, and Employee inherits from Person.

---

## 9. Hierarchical Inheritance

Multiple children inherit from the same parent.

```text
          Person
         /      \
        v        v
    Student   Employee
```

Example:

```python
class Person:

    def show(self):
        print("Person")


class Student(Person):

    def study(self):
        print("Studying")


class Employee(Person):

    def work(self):
        print("Working")
```

Both Student and Employee inherit `show()`.

---

## 10. Multiple Inheritance

One child inherits from multiple parents.

```python
class Father:

    def father_info(self):
        print("Father")


class Mother:

    def mother_info(self):
        print("Mother")


class Child(Father, Mother):

    def child_info(self):
        print("Child")


child = Child()

child.father_info()
child.mother_info()
child.child_info()
```

Output:

```text
Father
Mother
Child
```

Structure:

```text
Father       Mother
    \         /
     \       /
      Child
```

Python supports multiple inheritance.

---

## 11. Parent Order in Multiple Inheritance

The order matters.

```python
class Child(Father, Mother):
    pass
```

is different from:

```python
class Child(Mother, Father):
    pass
```

When both parents have the same method, Python uses MRO to decide which implementation is found first.

---

## 12. Method Overriding

Method overriding means the child provides its own implementation of a parent method.

```python
class Person:

    def show(self):
        print("Person")


class Student(Person):

    def show(self):
        print("Student")


student = Student()
student.show()
```

Output:

```text
Student
```

Python searches the child class first.

---

## 13. Why Method Overriding is Useful

A parent can provide general behavior.

```python
class Employee:

    def work(self):
        print("Employee works")
```

A child can customize it:

```python
class Developer(Employee):

    def work(self):
        print("Developer writes code")
```

Another child can have different behavior:

```python
class Manager(Employee):

    def work(self):
        print("Manager manages the team")
```

---

## 14. Calling the Parent Method

Sometimes the child overrides a method but still wants the parent implementation.

```python
class Person:

    def show(self):
        print("Person")


class Student(Person):

    def show(self):
        super().show()
        print("Student")


student = Student()
student.show()
```

Output:

```text
Person
Student
```

---

## 15. What is super()?

`super()` is used to continue method lookup according to the Method Resolution Order (MRO).

In simple inheritance:

```text
B -> A -> object
```

So:

```python
super().show()
```

inside B normally reaches A.

Important:

> `super()` does not simply mean "call my parent".

The more accurate meaning is:

> Continue method lookup according to the MRO.

This becomes very important in multiple inheritance.

---

## 16. Constructor Inheritance

If a child does not define `__init__()`, it can use the inherited constructor.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


student = Student("Laxman")

print(student.name)
```

Output:

```text
Laxman
```

---

## 17. What Happens When Child Defines __init__()?

If the child defines its own constructor, the parent constructor is not automatically executed.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, age):
        self.age = age
```

Now the child initializes `age`, but `name` is not initialized by Person.

---

## 18. Calling Parent Constructor with super()

Use:

```python
super().__init__()
```

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, age):

        super().__init__(name)
        self.age = age


student = Student("Laxman", 16)

print(student.name)
print(student.age)
```

Output:

```text
Laxman
16
```

---

## 19. Constructor Chaining

Constructor chaining means constructors call the next constructor in the inheritance hierarchy.

```python
class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, employee_id):

        super().__init__(name)
        self.employee_id = employee_id


class Manager(Employee):

    def __init__(self, name, employee_id, team_size):

        super().__init__(name, employee_id)
        self.team_size = team_size
```

Calling:

```python
manager = Manager("Laxman", 101, 10)
```

creates the chain:

```text
Manager.__init__()
        |
        v
Employee.__init__()
        |
        v
Person.__init__()
```

---

## 20. Python super() vs Java super()

In Java, `super()` is commonly used to invoke the parent constructor.

In Python:

```python
super().__init__()
```

calls the next constructor according to the MRO.

Python does **not** require `super().__init__()` to literally be the first statement of a constructor.

Example:

```python
class Student(Person):

    def __init__(self, name, age):

        self.age = age
        super().__init__(name)
```

This is valid Python.

The important thing is whether the order makes logical sense for the program.

---

## 21. Multiple Inheritance with Same Method

Consider:

```python
class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass
```

Both parents have `show()`.

Python uses MRO.

---

## 22. MRO

MRO means:

**Method Resolution Order**

It is the order in which Python searches classes for methods and attributes.

For:

```python
class Child(Father, Mother):
```

the MRO is approximately:

```text
Child
  |
Father
  |
Mother
  |
object
```

Python finds `show()` in Father first.

Therefore:

```text
Father
```

is printed.

---

## 23. Changing Parent Order

If we write:

```python
class Child(Mother, Father):
    pass
```

the MRO becomes:

```text
Child
  |
Mother
  |
Father
  |
object
```

Now Mother.show() is found first.

Therefore:

```text
Mother
```

is printed.

---

## 24. Checking MRO with mro()

Use:

```python
print(Child.mro())
```

Example:

```python
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.mro())
```

Important order:

```text
C -> A -> B -> object
```

---

## 25. Checking MRO with __mro__

We can also use:

```python
print(C.__mro__)
```

`mro()` returns the MRO as a list.

`__mro__` exposes the MRO as a tuple.

---

## 26. Diamond Inheritance

Diamond inheritance occurs when two classes inherit from the same parent and another class inherits from both.

```text
        A
       / \
      B   C
       \ /
        D
```

Example:

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

---

## 27. Diamond Problem

Without a proper method resolution system, Python would have to decide whether D should search:

```text
B
C
A
```

or some other order.

Python solves this using MRO.

---

## 28. Diamond MRO

For:

```python
class D(B, C):
```

the MRO is:

```text
D -> B -> C -> A -> object
```

This is one of the most important Day 14 concepts.

---

## 29. Program 35 — Multiple Inheritance with super() and MRO

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()

print(D.mro())

obj.show()
```

MRO:

```text
D -> B -> C -> A -> object
```

Output from `obj.show()`:

```text
A
C
B
D
```

---

## 30. Why Does B's super() Go to C?

This was a very important question.

B directly inherits from A:

```python
class B(A):
```

It is tempting to think:

```text
B -> A
```

But the object is a D object:

```python
obj = D()
```

D inherits:

```python
class D(B, C):
```

Therefore the complete MRO is:

```text
D -> B -> C -> A -> object
```

When `super()` is used inside B, Python continues from B in the complete MRO.

So:

```text
B -> C
```

not:

```text
B -> A
```

This is the key idea:

> `super()` follows the MRO of the complete inheritance hierarchy.

---

## 31. Step-by-Step Execution of Program 35

Call:

```python
obj.show()
```

Python starts at D.

### Step 1 — D.show()

```python
super().show()
```

Next class in MRO is B.

So:

```text
D -> B
```

### Step 2 — B.show()

B executes:

```python
super().show()
```

Next class in MRO after B is C.

So:

```text
B -> C
```

### Step 3 — C.show()

C executes:

```python
super().show()
```

Next class is A.

So:

```text
C -> A
```

### Step 4 — A.show()

A prints:

```text
A
```

Then A returns.

### Step 5 — Back to C

C now executes:

```python
print("C")
```

So:

```text
C
```

### Step 6 — Back to B

B now executes:

```python
print("B")
```

So:

```text
B
```

### Step 7 — Back to D

D now executes:

```python
print("D")
```

So:

```text
D
```

Final output:

```text
A
C
B
D
```

---

## 32. Why Output is A C B D

The method call chain is:

```text
D -> B -> C -> A
```

But every method calls `super()` BEFORE its own print.

Therefore the deepest method prints first:

```text
A
```

Then execution returns:

```text
C
B
D
```

So final output:

```text
A
C
B
D
```

Think of it like entering rooms and then coming back:

```text
Enter D
  Enter B
    Enter C
      Enter A
      Print A
    Print C
  Print B
Print D
```

---

## 33. Single Inheritance super() vs Multiple Inheritance super()

Single inheritance:

```text
B -> A
```

So:

```python
super().show()
```

inside B reaches A.

Multiple inheritance:

```text
D -> B -> C -> A
```

So:

```python
super().show()
```

inside B reaches C.

Therefore:

> The meaning of super() depends on the MRO.

---

## 34. Cooperative Multiple Inheritance

Classes can cooperate by consistently using:

```python
super()
```

instead of directly calling a specific parent.

Example:

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")
```

Every class participates in the chain.

This is called cooperative multiple inheritance.

---

## 35. Explicit Parent Method Call

Instead of:

```python
super().show()
```

we can explicitly call a parent:

```python
Father.show(self)
```

Example:

```python
class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):

    def show(self):

        Father.show(self)
        Mother.show(self)

        print("Child")
```

Output:

```text
Father
Mother
Child
```

---

## 36. super() vs Explicit Parent Call

### super()

```python
super().show()
```

Means:

> Continue according to MRO.

### Explicit call

```python
Father.show(self)
```

Means:

> Call Father's implementation specifically.

For cooperative multiple inheritance, `super()` is generally preferred.

---

## 37. C3 Linearization

Python uses an algorithm called **C3 Linearization** to calculate MRO.

Interview-level definition:

> C3 Linearization is the algorithm Python uses to create a consistent Method Resolution Order for classes, especially with multiple inheritance.

You normally do not implement C3 manually.

You mainly need to understand the resulting MRO.

---

## 38. isinstance()

`isinstance()` checks whether an object is an instance of a class.

Syntax:

```python
isinstance(object, class)
```

Example:

```python
class Person:
    pass


class Student(Person):
    pass


student = Student()

print(isinstance(student, Student))
print(isinstance(student, Person))
```

Output:

```text
True
True
```

A Student is also a Person because Student inherits from Person.

---

## 39. issubclass()

`issubclass()` checks whether one class is derived from another.

Example:

```python
class Person:
    pass


class Student(Person):
    pass


print(issubclass(Student, Person))
```

Output:

```text
True
```

---

## 40. isinstance() vs issubclass()

### isinstance()

Works with an object:

```python
student = Student()

isinstance(student, Student)
```

### issubclass()

Works with classes:

```python
issubclass(Student, Person)
```

Memory trick:

```text
isinstance -> object
issubclass -> class
```

---

## 41. isinstance() with Multiple Inheritance

```python
class Employee:
    pass


class Developer:
    pass


class SoftwareEngineer(Employee, Developer):
    pass


engineer = SoftwareEngineer()

print(isinstance(engineer, SoftwareEngineer))
print(isinstance(engineer, Employee))
print(isinstance(engineer, Developer))
```

Output:

```text
True
True
True
```

---

## 42. object Class

Python classes ultimately inherit from `object`.

For example:

```text
Student
   |
Person
   |
object
```

Therefore MRO commonly ends with:

```text
object
```

Example:

```python
print(Student.mro())
```

can show:

```text
Student
Person
object
```

---

## 43. What Happens When a Method is Not Found?

Python searches according to MRO.

Example:

```python
class A:

    def show(self):
        print("A")


class B(A):
    pass


obj = B()

obj.show()
```

Search:

```text
B -> A -> object
```

`show()` is found in A.

Output:

```text
A
```

If the method cannot be found anywhere in the MRO, Python raises `AttributeError`.

---

## 44. Common Mistake — Forgetting super().__init__()

Incorrect:

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, age):
        self.age = age
```

Parent initialization is skipped.

Correct:

```python
class Student(Person):

    def __init__(self, name, age):

        super().__init__(name)
        self.age = age
```

---

## 45. Common Mistake — Thinking super() Means Immediate Parent

Incorrect mental model:

```text
super() = always call immediate parent
```

Correct:

```text
super() = continue according to MRO
```

This is especially important in multiple inheritance.

---

## 46. Common Mistake — Ignoring Parent Order

These can produce different MROs:

```python
class Child(A, B):
    pass
```

and:

```python
class Child(B, A):
    pass
```

Always check the MRO when multiple inheritance is involved.

---

## 47. Common Mistake — Direct Parent Calls

Using:

```python
A.show(self)
```

directly selects A.

It can bypass other classes that should participate in cooperative multiple inheritance.

When the hierarchy is designed for cooperative inheritance, prefer:

```python
super().show()
```

---

## 48. Common Mistake — Forgetting self in Explicit Calls

Incorrect:

```python
Father.show()
```

Correct:

```python
Father.show(self)
```

Or use:

```python
super().show()
```

when appropriate.

---

## 49. Practical Example — Person and Student

```python
class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, age):

        self.age = age
        super().__init__(name)

    def display_name(self):

        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Laxman", 16)

student.display_name()
```

Output:

```text
Name: Laxman
Age: 16
```

Important:

```python
self.age = age
super().__init__(name)
```

is valid Python.

---

## 50. Practical Employee Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)


class Developer(Employee):

    def show(self):
        super().show()
        print("Developer")


class Manager(Employee):

    def show(self):
        super().show()
        print("Manager")
```

This demonstrates:

- inheritance
- overriding
- `super()`

---

## 51. Practical Multiple Roles Example

```python
class Employee:

    def employee_info(self):
        print("Employee")


class Developer:

    def developer_info(self):
        print("Developer")


class Manager:

    def manager_info(self):
        print("Manager")


class TechLead(Employee, Developer, Manager):

    def techlead_info(self):
        print("Tech Lead")


tech_lead = TechLead()

tech_lead.employee_info()
tech_lead.developer_info()
tech_lead.manager_info()
tech_lead.techlead_info()
```

Output:

```text
Employee
Developer
Manager
Tech Lead
```

---

## 52. Python vs Java Inheritance

Python supports multiple class inheritance:

```python
class Child(Father, Mother):
    pass
```

Java does not allow:

```java
class Child extends Father, Mother
```

Java uses interfaces to achieve multiple inheritance of type/behavior.

---

## 53. Important Java vs Python super() Difference

Java:

```java
super();
```

is commonly used for the parent constructor.

Python:

```python
super().__init__()
```

continues constructor lookup according to MRO.

In simple inheritance, this normally reaches the parent.

In multiple inheritance, it can reach another class in the MRO.

---

## 54. Output Prediction Example 1

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


obj = B()
obj.show()
```

MRO:

```text
B -> A -> object
```

Output:

```text
A
B
```

---

## 55. Output Prediction Example 2

```python
class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.show()
```

MRO:

```text
C -> A -> B -> object
```

Output:

```text
A
```

---

## 56. Output Prediction Example 3

```python
class A:

    def show(self):
        print("A")


class B:

    def show(self):
        print("B")


class C(B, A):
    pass


obj = C()
obj.show()
```

MRO:

```text
C -> B -> A -> object
```

Output:

```text
B
```

---

## 57. Output Prediction Example 4 — Diamond

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()
obj.show()
```

MRO:

```text
D -> B -> C -> A -> object
```

Output:

```text
A
C
B
D
```

---

## 58. How to Solve MRO Interview Questions

### Step 1

Write the inheritance hierarchy.

### Step 2

Find the MRO.

### Step 3

Find where the requested method is first found.

### Step 4

If `super()` is present, move to the next class in MRO.

### Step 5

Continue until the chain ends.

### Step 6

Pay attention to code before and after `super()`.

Example:

```python
super().show()
print("B")
```

The print happens after the next method finishes.

---

## 59. Important Mental Model for super()

For:

```python
def show(self):

    super().show()
    print("B")
```

Think:

```text
Go to next class
      |
      v
execute its method
      |
      v
return
      |
      v
print B
```

This is why the diamond example prints:

```text
A
C
B
D
```

---

## 60. The Most Important Day 14 Example

Remember:

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()

print(D.mro())

obj.show()
```

MRO:

```text
D -> B -> C -> A -> object
```

Call chain:

```text
D -> B -> C -> A
```

Output:

```text
A
C
B
D
```

---

## 61. Why B Does Not Directly Call A

B is declared as:

```python
class B(A):
```

But the object is an instance of D.

D's complete MRO is:

```text
D -> B -> C -> A -> object
```

Therefore inside B:

```python
super().show()
```

means:

> Find the next `show()` after B in the MRO.

The next class is C.

Therefore:

```text
B -> C
```

This is one of the most important concepts to remember from Day 14.

---

## 62. Important Rules to Memorize

### Rule 1

Inheritance allows code reuse.

### Rule 2

A child can override a parent method.

### Rule 3

If a child defines its own `__init__()`, the parent constructor is not automatically executed.

### Rule 4

Use:

```python
super().__init__()
```

to continue constructor initialization.

### Rule 5

`super()` follows MRO.

### Rule 6

Python supports multiple inheritance.

### Rule 7

Parent order matters.

### Rule 8

Use `mro()` or `__mro__` to inspect MRO.

### Rule 9

Python uses C3 Linearization for MRO.

### Rule 10

`super()` does not simply mean "my parent".

---

## 63. Quick Comparison Table

| Concept | Meaning |
|---|---|
| Parent class | Class being inherited from |
| Child class | Class that inherits |
| Inheritance | Reusing parent functionality |
| Method overriding | Child changes parent method |
| `super()` | Continues according to MRO |
| Multiple inheritance | Child has multiple parents |
| MRO | Method search order |
| Diamond inheritance | Shared parent inheritance structure |
| C3 Linearization | MRO calculation algorithm |
| `isinstance()` | Checks object |
| `issubclass()` | Checks class |
| `mro()` | Displays MRO |
| `__mro__` | MRO tuple |
| `object` | Ultimate base class |

---

## 64. Interview Question — What is inheritance?

Answer:

> Inheritance allows a child class to acquire properties and methods from a parent class.

---

## 65. Interview Question — What is method overriding?

Answer:

> Method overriding occurs when a child class provides its own implementation of a method defined in the parent class.

---

## 66. Interview Question — What is super()?

Answer:

> `super()` continues method or attribute lookup according to the Method Resolution Order.

---

## 67. Interview Question — Does super() always call the immediate parent?

Answer:

> No. It follows the MRO. In simple inheritance the next class is usually the parent, but in multiple inheritance it can be another class in the MRO.

---

## 68. Interview Question — Does Python support multiple inheritance?

Answer:

> Yes. Python allows a class to inherit from multiple classes.

Example:

```python
class Child(Father, Mother):
    pass
```

---

## 69. Interview Question — What is MRO?

Answer:

> MRO stands for Method Resolution Order. It defines the order in which Python searches classes for methods and attributes.

---

## 70. Interview Question — What is diamond inheritance?

Answer:

> Diamond inheritance occurs when two classes inherit from the same parent and another class inherits from both of those classes.

Structure:

```text
        A
       / \
      B   C
       \ /
        D
```

---

## 71. Interview Question — How does Python solve the diamond problem?

Answer:

> Python uses Method Resolution Order based on C3 Linearization to create a consistent method lookup order.

---

## 72. Interview Question — What is the difference between isinstance() and issubclass()?

Answer:

> `isinstance()` checks whether an object is an instance of a class. `issubclass()` checks whether one class inherits from another class.

---

## 73. Interview Question — What is the difference between super() and direct parent calls?

Answer:

> `super()` continues according to MRO, while a direct call such as `A.show(self)` specifically calls A's implementation.

---

## 74. Interview Question — What is cooperative multiple inheritance?

Answer:

> Cooperative multiple inheritance is a design where classes use `super()` so that every class in the MRO can participate in method execution.

---

## 75. Interview Question — What is C3 Linearization?

Answer:

> C3 Linearization is the algorithm Python uses to calculate a consistent MRO, especially for multiple inheritance.

---

## 76. Day 14 Final Revision

The learning sequence is:

```text
Inheritance
     |
     v
Parent / Child
     |
     v
Types of Inheritance
     |
     v
Method Overriding
     |
     v
Constructors
     |
     v
super()
     |
     v
Multiple Inheritance
     |
     v
MRO
     |
     v
Diamond Inheritance
     |
     v
C3 Linearization
     |
     v
Cooperative Multiple Inheritance
     |
     v
isinstance()
     |
     v
issubclass()
```

---

## 77. Day 14 — Most Important Concept

If you remember only one thing from Day 14, remember:

```text
super() -> follows MRO
```

Not:

```text
super() -> always calls my parent
```

For:

```python
class D(B, C):
```

and:

```text
D -> B -> C -> A -> object
```

then:

```text
super() inside D -> B
super() inside B -> C
super() inside C -> A
```

---

## 78. Day 14 — Final MRO Example

```text
        A
       / \
      B   C
       \ /
        D
```

MRO:

```text
D -> B -> C -> A -> object
```

Method execution:

```text
D.show()
   |
   v
B.show()
   |
   v
C.show()
   |
   v
A.show()
```

Because each method prints after `super()`:

```text
A
C
B
D
```

---

## 79. Day 14 Completion Checklist

- [x] Inheritance
- [x] Parent class
- [x] Child class
- [x] Code reuse
- [x] Single inheritance
- [x] Multilevel inheritance
- [x] Hierarchical inheritance
- [x] Multiple inheritance
- [x] Method overriding
- [x] Parent method calling
- [x] `super()`
- [x] Constructor inheritance
- [x] Constructor overriding
- [x] `super().__init__()`
- [x] Constructor chaining
- [x] Same method in multiple parents
- [x] Parent ordering
- [x] MRO
- [x] `mro()`
- [x] `__mro__`
- [x] Diamond inheritance
- [x] Diamond problem
- [x] C3 Linearization
- [x] Cooperative multiple inheritance
- [x] Explicit parent calls
- [x] `isinstance()`
- [x] `issubclass()`
- [x] Python vs Java inheritance
- [x] Common mistakes
- [x] MRO output tracing
- [x] Interview questions

---

## 80. Day 14 Final Summary

Day 14 teaches the inheritance system used by Python.

The most important concepts are:

```text
Inheritance
Method Overriding
super()
Multiple Inheritance
MRO
Diamond Inheritance
C3 Linearization
```

The most important example is:

```text
D -> B -> C -> A -> object
```

and the output:

```text
A
C
B
D
```

The most important rule is:

> `super()` follows the MRO, not simply the immediate parent.

This understanding is the foundation for advanced Python OOP and is important before moving to more advanced Python topics.
