statusCode = 200
myName = 'John'

if myName != 'John':
    print('Hello, ' + statusCode)
elif myName == 'John':
    print('Hello, ' + myName + " your status code is " + str(statusCode))
else:
    print("something went wrong")

