def divide_by(a, b):
    return a / b

try: 
    ans = divide_by(40, 0)
except Exception as e: 
    print("Something went wrong", e)

    
    
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')

ans = divide_by(10,0)
print(ans)


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  
