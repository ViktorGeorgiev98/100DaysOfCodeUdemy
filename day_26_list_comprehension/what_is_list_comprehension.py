# create new list from a list, but each number is increase by 1
# numbers = [1, 2, 3]
# new_list = [num + 1 for num in numbers]
# first parameter is the result you wish => number + 1
# second parameter is each item in the list
# third parameter is the list
# print(new_list)
import random

# train it
# numbers = [5, 12, 50, 34]
# numbers_multiplied_by_3 = [num * 3 for num in numbers]
# print(numbers_multiplied_by_3)

# you can do it with strings, works the same way, but you will get a split string into a list
# name = "Viktor"
# name_in_upper = [letter.upper() for letter in name]
# print(name_in_upper)


# create new list using in range, same as a list which is a variable but we use range
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# conditional list comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# new_list = [name for name in names if len(name) < 5]
# print(new_list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [num / 2 for num in numbers if num % 2 == 0]
# print(new_list)

# new_list = [num / 2 for num in range(1, 11) if num % 2 == 0]
# print(new_list)


# Dictionary comprehension (objects) using dictionaries (arrays)
# list = [1, 2, 3, 4]
# new_dict = {"num":item for item in list}
# print(new_dict)


# Dictionary comprehension (objects) using dictionaries (objects)
# dict = {
#     "num1": 1,
#     "num2": 2,
#     "num3": 3,
#     "num4": 4,
# }
# new_dict = {key:value * 2 for (key, value) in dict.items()}
# print(new_dict)


# more training
# names = ["Alex", "Beth", "Caroline", "Dave", "Freddie"]
# students_scores = {student:random.randint(1, 101) for student in names}
# print(students_scores)
# passed_students = {student:score for (student,score) in students_scores.items() if score > 50}
# for student in passed_students:
#     print(f"Score of {student} => {passed_students[student]}")


# how to iterate through a pandas data frame
# import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     key => column name
# value => data in each column

# pandas has built in loop
# correct way!!!
# for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    # if row.student == "Angela":
    #     print(row.score)


