# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data_list = []
# #     data = csv.reader(data_file)
# #     for each in data:
# #         data_list.append(each)
# #     # print(data)
# #
# # print(data_list[0][1])
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data.condition)
# print(type(data.condition))
# print(type(data))
# print(data.to_dict())
# temp_list = data.temp.to_list()
# print(temp_list)
#
# """ finding average of temperature """
#
# print(sum(temp_list))
# total = 0
# for each in temp_list:
#     total += each
# print(total)
# average_temp = total/len(temp_list)
# print(average_temp)
# print(data.temp.mean())
#
# print(data[data.day == "Monday"])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_fah = (monday_temp * 9/5) + 32
# print(monday_temp_fah)
# print(data[data.temp == data.temp.max()])
#
#
# data_dict = {
#     "students": ["arun", "krish", "jack"],
#     "age": [23, 22, 21]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("nww_data.csv")

""" ABOVE CODE IS LEARNING HOW TO ACESS CSV USING PANDAS AND NORMAL METHOD"""


"""BELOW CODE IS WORKING WITH SQUIREEL DATA OF NEW YORK CITY"""

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])


dict_data = {
    "squirrels" : ["Gray", "Cinnamon", "Black"],
    "counts" : [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(dict_data)
new_data.to_csv("squirrel_count.csv")

print(dict_data)
