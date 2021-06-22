import re
from challenges.hashtable.hashtable import Hashtable
def spliting(str):
    str = str.replace(',','')
    list_str = str.split(' ')
    
    return list_str

def repeated_word(input):
    hashmap = Hashtable()

    words_list = spliting(input)
    for word in words_list:
        lower_word = word.lower()
        if hashmap.contains(lower_word):
            return lower_word
        hashmap.add(lower_word, 1)


#     duplicates_list=[]
#     # print(input, "before regex")
#     input = re.sub(r"[^A-z|\s]", '', input)
#     # print(input, "after regex")
#     input = input.lower()
#     input = input.split()
#     # print(input)
#     for i in input:
#         if i in duplicates_list :
#             return i
#         else:
#             duplicates_list.append(i)

# print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))