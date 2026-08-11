# Day 15 Notes

## Topics
- Encapsulation and private attributes
- `__dict__`
- Name mangling
- Getters and setters
- `@property`
- Read-only properties
- Calculated properties
- Validation with `strip()`
- Inheritance and property inheritance
- Property overriding
- `super()` with properties
- `fget` and `fset`
- Reusing a parent's setter
- Private attributes with inheritance
- BankAccount/SavingsAccount mini-project

## Key Rules

A property is accessed without parentheses:
```python
employee.salary
```

A setter is used by assignment:
```python
employee.salary = 50000
```

A property without a setter is read-only.

`strip()` removes leading/trailing whitespace. Therefore:
```python
if value.strip():
```
rejects an input containing only spaces.

For a property:
- `fget` is the getter function.
- `fset` is the setter function.

A child class that overrides a property does not automatically get the parent's setter for that new property.

Parent setter reuse:
```python
Person.name.fset(self, value)
```

If a parent has:
```python
self.__balance
```
the mangled name is:
```python
self._BankAccount__balance
```
A child should normally use the inherited public property:
```python
self.balance
```
rather than trying to access the parent's private storage directly.
