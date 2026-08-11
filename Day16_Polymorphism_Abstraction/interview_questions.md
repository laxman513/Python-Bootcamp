# Day 16 - Interview Questions

## 1. What is polymorphism?

Polymorphism means the same interface or operation can produce different behavior for different objects.

## 2. What is method overriding?

When a child class provides its own implementation of a method inherited from the parent class.

## 3. What is duck typing?

Duck typing means Python determines whether an object can be used based on the methods/behavior it provides rather than its class type.

## 4. What is an abstract class?

A class intended to act as a blueprint. It can contain abstract methods that concrete subclasses must implement.

## 5. How do you create an abstract class in Python?

```python
from abc import ABC

class Payment(ABC):
    pass
```

## 6. What is @abstractmethod?

It marks a method as abstract. A concrete subclass must implement it before its object can normally be created.

## 7. Can an abstract class contain normal methods?

Yes.

```python
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Sleeping")
```

## 8. Can an abstract class contain properties?

Yes.

```python
@property
@abstractmethod
def salary(self):
    pass
```

## 9. Why is salary accessed as employee.salary?

Because `salary` is defined using `@property`.

## 10. Why is process called as payment.process()?

Because `process` is a normal method, not a property.

## 11. What happens if a child doesn't implement an abstract method?

The child remains abstract and its object cannot normally be instantiated.

## 12. What is super()?

It is used to access the parent class implementation.

## 13. What does key do in sorted()?

It specifies the value/function used to determine sorting order.

## 14. What does this mean?

```python
sorted(employees, key=lambda employee: employee.salary)
```

It sorts Employee objects according to their salary.

## 15. Can functions be passed as arguments?

Yes. Functions are first-class objects in Python.

Example:

```python
calculate(square, 5)
```

## 16. Abstract class vs interface in Java

Python ABCs can provide both abstract methods and concrete methods, similar to an abstract class in Java. Python also uses ABCs to model interface-like contracts.

## 17. Why is polymorphism useful?

It allows code to work with different implementations without writing separate logic for every concrete class.

## 18. What is the main advantage of abstraction?

It hides implementation details and forces concrete classes to provide required behavior.
