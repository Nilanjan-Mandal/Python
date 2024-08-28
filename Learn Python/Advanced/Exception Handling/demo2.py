def add_number(num1, num2):
    try:
        if (isinstance(num1,int) or (isinstance(num1, float) and isinstance(num2,int) or (isinstance(num2, float)))):
            return (num1 + num2)
        else:
            raise Exception('Only int and float values are allowed')
    except Exception as e:
        return e
        
print(add_number(1,2))
print(add_number(10,80))
print(add_number(10,'b'))
print(add_number('c','d'))
print("Execution Successful")