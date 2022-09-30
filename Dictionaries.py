'Dictionaries'

''' create a dictionary “students” with many dictionaries in them 
like the “student” dictionary in the video. Use a number ID as the key of each student.

Then try to create a class Student containing the same data as each “student” dictionary 
and store the instances of those Student classes in the “students” dictionary.

Then make a function “filter_age” that returns a list of all students 
with an age >= the input variable “min_age”. Use the “students” dictionary from the global scope 
and return a new dictionary with the same structure, but with the filtered age.'''

# add keys and data {'key': data,}
# overwrite update dictionary with .update({'newkey': newdata, 'key': newdata})
# delete keys using del 'key'
# delete and assign to a variable using .pop('key')
# get only the values .values()
# get keys and values .items() which returns tuples of keys and values
# for key in dictionary only loops through the keys



students = {}

class Student:
    def __init__(self, student_ID, name, age, courses):
        ''' Student_ID is 8 letter string S and them 7 numbers, name is a string, 
        age an integer and courses a list of strings.'''
        self.name = name
        self.age = age
        self.courses = courses
        self.student_ID = student_ID
        students.update({student_ID: {'name': name, 'age': age, 'courses': courses}})

def filter_age(min_age):
    filter_students = {}
    for key, value in students.items():
        if value.get('age') >= min_age:
            filter_students.update({key: value})
    return filter_students

Lucy_Spouncer = Student('S2020746', 'Lucy Spouncer', 20, ['Mathematics'])
Daniel_Holler = Student('S2390845', 'Daniel Holler', 20, ['Computer Science', 'Electronic Engineering'])
Sofie_Davidson = Student('S4935432', 'Sofie Davidson', 19, ['Physics', 'Danish', ])
Pablo_Sandquist = Student('S2352143', 'Pablo Sandquist', 19, ['Physics', 'Astrophysics'])

older_students = filter_age(20)

print(older_students)

# '''Or instead we do this...'''

# students = {}

# class Student:
#     def __init__(self, student_ID, name, age, courses):
#         ''' Student_ID is 8 letter string S and them 7 numbers, name is a string, 
#         age an integer and courses a list of strings.'''
#         self.name = name
#         self.age = age
#         self.courses = courses
#         self.student_ID = student_ID

#         students.update(student_ID: self)

