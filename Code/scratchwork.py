import string

if __name__ == '__main__':
#     print('{0:08b}'.format(6))
#     print(int("10011101", base=2))

# #binary search
# lst = [2,3,5,7,11,22,25]
# total = sum(lst)
# length = len(lst)
# middle = total/length
# end = length -1
# print(end)

    text = "!bananas! apples"
    text = text.casefold().replace(" ", "")
    remove_punct = str.maketrans("","", string.punctuation)
    text = text.translate(remove_punct)
    patt = "b"
    # def get_index(strin, pattern):
    #     for index in strin:
    #         if pattern in strin: return strin.index(pattern)
    # reverse_text = ""

    text_ls = text.split()
    print(text_ls)
    # for char in text:
    #     reverse_text = char + reverse_text
    # print(get_index(text, patt))

