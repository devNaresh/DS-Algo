__author__ = '__naresh__'

# Implementation of Rabin Karp substring Search

"""

Time Complexibility O(m*n)

https://www.youtube.com/watch?v=H4VrKHVG5qI

Application -- Generally used for serching of multiple patterns

"""

PRIME_NUMBER = 101


def create_hash(pattern):
    length = len(pattern)
    hash = 0
    for x in range(length):
        hash += (PRIME_NUMBER ** x) * ord(pattern[x])
    return hash


def recreate_hash(old_hash, orignal_string, postion, pattern_len):
    """
    For generating new hash from old hash follow below three steps
        1) Minus value of element which got out from pattern
        2) Divide new hash value with prime number
        3) Added new value with new hash value

    """
    if old_hash is 0:
        return create_hash(orignal_string[:pattern_len])
    else:
        value = ord(orignal_string[postion + pattern_len - 1]) * (PRIME_NUMBER ** (pattern_len - 1))
        new_hash = old_hash - ord(orignal_string[postion - 1])
        new_hash /= PRIME_NUMBER
        new_hash += value
        return new_hash


def find_substing(orignal_string, pattern):
    pattern_hash = create_hash(pattern)
    string_hash = 0
    for i in range(len(orignal_string) - len(pattern)):
        string_hash = recreate_hash(string_hash, orignal_string, i, len(pattern))
        if string_hash == pattern_hash:
            found = True
            for x, y in zip(orignal_string[i:i + len(pattern)], pattern):
                if x != y:
                    found = False
                    break
            if found: return i
    return None


if __name__ == "__main__":
    data = "jim saw me in a barber parlour"
    pattern = "barber"
    start = find_substing(data, pattern)
    end = start + len(pattern)
    print data[start:end]
