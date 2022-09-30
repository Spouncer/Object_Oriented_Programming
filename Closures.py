# when do we have closures?
''' - when we have a nested function
- when the nested function refers to a variable inside the enclosing function
- when the enclosing function returns the nested function'''

# # example
# def make_multiplier(n):

#     def multiplier(x):
#         return n*x

#     return multiplier

# times3 = make_multiplier(3)

# print(times3(10))

# print(make_multiplier(6)(7))

'''make a function that takes a string input and 
returns a function that takes a string and replaces all instances 
of the non-local input bu the same number of underscores '''

def make_editor(words):

    def editor(text):
        for string in words:
            n = len(string)

            sep_text = text.split(string)
            m = len(sep_text)

            new_text = sep_text[0]
            for i in range(1, m):
                word = sep_text[i].rjust(len(sep_text[i]) + n, '_')
                new_text = new_text + word
            text = new_text
        return new_text

    return editor

form = make_editor(['Lucy', '20', 'Maths', 'Edinburgh'])
string = 'Hi, my name is Lucy and I am 20 years old, I study Maths at Edinburgh University'
print(form(string))

print(form('I went to see Lucy for her birthday, she turned 20. Ive always wanted to visit Edinburgh.'))

