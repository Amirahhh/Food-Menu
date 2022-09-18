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

    
    def sum_of(**kwargs):
    sum = 0 
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))

# args you can pass in any argument of non-kyword variables
# with Kwargs, any amount of keyword arguments. 


# the following will open and close the file automatically
with open("text.txt", mode = "r") as file:
    data = file.readline()

    print(data)

#The following will open the doc and you have tp close it
file = open("text.txt" mode = "r")

data = file.readline()
print(data)

file.close()


#to open a file and append:(a). to overwrite: (w)
try:
    with open("newfile.txt", "a") as file:
        file writelines:(["\nThis is a new file created.", "\nThis is a new line"])
except FileNotFoundError as e:
    print("Error", e)
