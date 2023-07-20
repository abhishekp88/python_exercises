# read
with open('/Users/inapaliwal/Desktop/myfile.txt') as my_file:
    contents = my_file.read()
    print(contents)

with open('../../Desktop/myfile.txt') as my_file:
    contents = my_file.read()
    print(contents)

# write mode
with open('./myfile.txt',mode='w') as my_file:
    my_file.write("Update Fle TExt:")


# write mode
with open('myfile_new.txt',mode='w') as my_file:
    my_file.write("New Text:")


# absolute path
# start with origin


# relative path
# start with current point to destiantion