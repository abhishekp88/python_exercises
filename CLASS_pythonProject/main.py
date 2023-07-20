class User:
    # used when class or function are empty
    # used to define attriutes
    def __init__(self,id,name):
        self.name = name
        self.id = id
        self.followers = 0
        self.following = 0
    # mwthod define in class
    def printUserData(self):
        print(self.name)
        # print(self.id)
        print(f'followers {self.followers}')
        print(f'following {self.following}')

    def follow(self,user):
        user.followers += 1
        self.following +=1

user_1 = User(1,'Abhishek')
user_2 = User(2,'Manish')
print(user_1)

user_1.follow(user_2)
user_1.printUserData()
user_2.printUserData()
# create attributes
# user_1.id = 1
# user_1.name = 'Abhishek'
# print(user_1.id)
# print(user_1.name)
# print(user_1.followers)


# create attributes manually
# user_2.id = 2
# user_2.name = 'Manish'
# print(user_2.id)
# print(user_2.name)

# constructor
#  use to define attributes when object is being constructed (initialz value or method
# def __init__(self)  this function is used to initialize attributes, special functions
# init function will call every time construction happens mean new object construction

