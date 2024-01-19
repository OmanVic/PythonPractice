# with open("file1.txt") as file1:
#     read_file1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     read_file2 = file2.readlines()
#
# result = [int(number) for number in read_file1 if number in read_file2]
# print(result)

#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow "
# result = {item: len(item) for item in sentence.split()}
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

result = {days: (temp * 9/5) + 32 for (days, temp) in weather_c.items()}
print(result)
