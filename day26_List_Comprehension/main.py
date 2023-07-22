# create list fom previous list without loop
import random

# new_list = [new_item for item in list] syntax


numbers = [1, 2, 3]
new_list = []

new_list = [n+1 for n in numbers]

print(new_list)

name = "Angela"
new_name = [letter for letter in name]
print(new_name)

new_range = range(1,5)
final_range = [r *2 for r in new_range]
print(final_range)

# conditional comprehension

# new_list = [new_item for item in item_list if test]
final_range_test = [r1 *2 for r1 in range(1, 5) if r1%2 == 0]
print(final_range_test)

# dictionary comprehension

# new_dict =  {new_key: new_value for (key,value) in dict.items()}

random_number = {students: random.randint(1,100) for students in range(1, 5)}
print(random_number)

# dictonary conditional comprehension
sample_dict = {1: 22, 2: 65, 3: 69, 4: 27}
random_number_2 = {student: sample_dict[student] for student in sample_dict if sample_dict[student] > 60}
# these both work
random_number_1 = {student:score for (student,score) in sample_dict.items() if score > 60}
print(random_number_1)
print(random_number_2)



# iteration on panda data frame
student_dict = {
    'student': ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# loop through into row and get either complete valur or tap and get particular value
for (index,row) in student_data_frame.iterrows():
    print(row)
    # particular value
    print(row.student)
