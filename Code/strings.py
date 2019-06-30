#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    #Runtime of O(n*2) due to get_indexes
    
    if pattern == "": #O(1)
        return True

    get_indexes = find_all_indexes(text, pattern) #O(n)

    if get_indexes: #O(1)
        return True
    return False
  
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    #O(n *2) due to get_indexes

    
    if pattern  == "": #O(1)
        return 0

    get_indexes = find_all_indexes(text, pattern) #O(n)

    if get_indexes: #O(1)
            return get_indexes[0]

    return None
    
    

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    index_lst = [] #O(1)
    count = 0 #O(1)

    if pattern == "":
        while count <= len(text)-1: #O(n)
            index_lst.append(count)
            count+=1
        return index_lst

    # if pattern == "":
    #     return index_lst

    for index, letter in enumerate(text): #O(n)
        if letter == pattern[0]:
            if text[index: index + len(pattern)] == pattern:
                index_lst.append(index)
            else: continue

    return index_lst #0(1)

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
