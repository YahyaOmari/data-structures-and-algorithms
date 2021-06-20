import re
def repeated_word(input):
    duplicates_list=[]
    # print(input, "before regex")
    input = re.sub(r"[^A-z|\s]", '', input)
    # print(input, "after regex")
    input = input.lower()
    input = input.split()
    # print(input)
    for i in input:
        if i in duplicates_list :
            return i
        else:
            duplicates_list.append(i)

print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))