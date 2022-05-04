# """filter name whose size is more than 5 and capital using single line"""
# name_list = ["arun", "krish", "dhoni", "spensar", "metric", "mclaraen" ]
# new_name_list = [each.upper() for each in name_list if len(each) > 5 ]
# print(new_name_list)

# """Squaring numbers using list comprehension in single line"""
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number*number for number in numbers]
# print(squared_numbers)


# """print only even numbers usig list comprehension"""
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [each for each in numbers if each % 2 == 0]
# print(result)


# """ using dictionary comprehension creating new dict key as string and value as length of string"""
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {each:len(each) for each in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:celsius* 9/5 + 32 for(day,celsius) in weather_c.items()}

print(weather_f)