def add_number(num1, num2):
    try:
        print(num1 + num2)
    except TypeError:
        return("Invalid Number")
    except Exception as e:
        return (e)
    else: 
        print("Successful...")
    finally:
        print('THE END ...')
        
add_number(1,'a')
