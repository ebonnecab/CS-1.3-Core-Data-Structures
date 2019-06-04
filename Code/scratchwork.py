if __name__ == '__main__':
    print('{0:08b}'.format(6))
    print(int("10011101", base=2))

#binary search
lst = [2,3,5,7,11,22,25]
total = sum(lst)
length = len(lst)
middle = total/length
end = length -1
print(end)

for index in range(length):
    print(lst)