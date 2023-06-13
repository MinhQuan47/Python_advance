try:
    x = 1/0
    print(x)
except TypeError:
    print("Data type of variable is not suitable type!")
except ZeroDivisionError:
    print("Cannot divide by 0!")
except:
    print("An exception occurred!")
