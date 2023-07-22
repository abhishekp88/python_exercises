def add(*args):
    # parameter in tuples
    print(args)
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(4, 5, 6, 7, 1, 2, 3)


'''
kwargs argument
** means we are  created unlimited keyword arguments
dictonary
'''
def calculate(**kwargs):
    # argument in dictonary
    print(kwargs)

    for key,value in kwargs.items():
        if key == 'add':
            kwargs[key] += kwargs[key]
        else :
            kwargs[key] *= kwargs[key]

    print(kwargs)

calculate(add=3, multiply=4)



class Car:

    def __init__(self, **kwargs):
        self.make = kwargs['make']
        '''
        if we dont have model attributes in kwargs, below line will give error
        '''
        # self.model = kwargs['model']

        '''
        if we dont have model attributes in kwargs, below line will not  give error it will return none, 
        will return value
        '''
        self.model = kwargs.get('model')

    def display_car(self):
        print(self.make, self.model)



# my_car = Car(make="nisan", model="micra")
my_car = Car(make="nisan")
my_car.display_car()