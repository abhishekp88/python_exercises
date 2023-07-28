'''
try: that might cause an exception

:except: block :- execute if there is an exception ( we can add multiple based on the error

else: :- execute if there is no exception

finally : do this no matter what
'''

# file not found

# handle with try catch
try:
    file = open('sample.txt')
    a_dict = {'key': 'Value'}
    print(a_dict['key'])
except FileNotFoundError:
    print(' m in except part')
    file = open('sample.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f'this key {KeyError} does not exist')
    print(f"key {error_message} does not exist")
else:
    print(file.read())

finally:
    file.close()
    print('this code will always execute')
    # raise is used to generate own exceptions
    # raise TypeError("This is error i made it")





height = float(input("Height: "))
weight = int(input("Weight: "))


if height > 3:
    raise ValueError("Human Height should not be more then 3 meters")
bmi = weight / height ** 2

print(bmi)





# key error
# a_dict = { 'key': 'Value'}
# val = a_dict['sample']

# index error
# fruit_list = ['1', '2', '3']
# print(fruit_list[3])

# type error
# text = 'abc'
# print(text + 5)

# try except, else , finally
