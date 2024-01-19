# # #The main errpr that commonly occur are the
# # #TypeError
# # #ValueError
# # #KeyError
# # #indexError
# #
# # #the format for error handling is
# #
# # #try
# # #except
# # #else
# # #finally
# #
# # #we can also raise our own error using the raise key word
# #
# # #       Trial
# # #
# # # try:
# # #     file1 = open("victor.txt")
# # #
# # #     a_dictionary = {"key": "value"}
# # #     print(a_dictionary)
# # #     print(a_dictionary["uve"])
# # #
# # # except FileNotFoundError:
# # #     file1 = open("victor.txt", "w")
# # #     file1.write("something")
# # # except KeyError:
# # #     a_dictionary["uve"] = "yre"
# # #
# # # else:
# # #     print("hutjtjht")
# #
# #
# # # TO RAISE AN ERROR
# #
# # height = int(input("What is the height"))
# # weight = int(input("what is the weight"))
# #
# # if height > 3:
# #     raise ValueError("Human height is not more than 3 meters.")
# #
# # bmi = weight / height ** 2
# #
# # print(bmi)
#
#
#
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass




print(total_likes)