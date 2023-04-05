# Accept a string and use list comprehension to generate as many strings of that word
# in an array as many letters are in the given string. For example:
# string = "Code" (4 letters in the string) --> ["Code", "Code", "Code", "Code"]


def create_list(morewords):
    return [morewords for i in range(len(morewords))]


print(create_list("Code"))  # should return the word "Code" 4 times
print(create_list("lovely"))  # should return the word "lovely" 6 times
