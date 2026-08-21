try:
    number = int("abc")

except ValueError:
    print("ValueError handled")

except Exception:
    print("General exception handled")