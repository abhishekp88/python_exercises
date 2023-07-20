with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)

import csv
# in built csv reading writing library
with open('weather_data.csv') as data_file:
    temperatures =[]
    data = csv.reader(data_file)
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
        # print(row)
    # print(temperatures)

# panda lib
import pandas
data = pandas.read_csv('weather_data.csv')
# print(data)
# print temp from data temp is column name in csv
# print(data['temp'])
# print(type(data['temp']))
# column is called as series in panda library

data_dict = data.to_dict()
# create each column dictinoary / object
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# to print avg or mean of complete column
print(data['temp'].mean())

# print max number in series
print(data['temp'].max())

print(data.condition)

#get data in row
print(data[data.day == 'Monday'])

# get row which have max temp
print(data[data.temp == data['temp'].max()])

day1 = data[data.temp == data['temp'].max()]
temp = day1['temp']
temp = temp * 9/5 + 32
print(temp)

print(temp)


# Create data frame
data_dict = {
    'students': ['A', 'B', 'C'],
    'scores': [76, 70, 45]
}
d = pandas.DataFrame(data_dict)
print(d)
# export data into csv
d.to_csv("new_data.csv")


sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
total_colors = sq_data['Primary Fur Color'].unique()
print(sq_data['Primary Fur Color'].unique())

count = []
for color in total_colors:
    # print(sq_data['Primary Fur Color'])
    count.append(len(sq_data[sq_data['Primary Fur Color'] == color]))
print(count)

sq_dict = {
    'Fur Color': total_colors,
    'Count': count
}
new_file = pandas.DataFrame(sq_dict)
new_file.to_csv("sq.csv")