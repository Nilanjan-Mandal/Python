def add_number(num1, num2):
    try:
        return (num1 + num2)
    # except TypeError:
    #     return("Invalid Number")
    # except NameError:
    #     return("Invalid Parameter")
    except Exception as e:
        return (e)
        
print(add_number(1,2))
print(add_number(10,80))
print(add_number(10,'b'))
print("Execution Successful")