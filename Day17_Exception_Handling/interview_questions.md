# Day 17 — Exception Handling Interview Questions

1. What is an exception in Python?
2. Error vs exception?
3. What are `try` and `except`?
4. Can one `try` have multiple `except` blocks?
5. What is `else` used for?
6. What is `finally` used for?
7. Can `else` and `finally` be used together?
8. Can `finally` exist without `except`?
9. What happens to statements after a `raise` inside `try`?
10. What does `except ValueError as error` mean?
11. What is `Exception`?
12. Why should specific exceptions come before `Exception`?
13. What is `raise`?
14. Automatic vs manual exception raising?
15. What is a custom exception?
16. Why inherit custom exceptions from `Exception`?
17. When should a function raise instead of handle an exception?
18. Why is bare `except:` usually discouraged?
19. How do you handle file exceptions?
20. What is exception propagation?
21. How would you design exceptions for a banking application?
22. Explain the Day 17 BankAccount exception flow.

### Strong interview summary
Python exception handling uses `try`, `except`, `else`, and `finally`. `try` contains risky code, `except` handles expected failures, `else` runs when no exception occurs, and `finally` is used for cleanup. `raise` explicitly signals an error, and custom exceptions make application-specific business failures clear.
