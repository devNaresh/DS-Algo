__author__ = "__naresh__"

# WAP to find maximmum sum of sbsequence in a arry such that elements are non adjacent

def find_max_sum(elements):
    inclusive = elements[0]
    exclusive = 0

    for i in range(1, len(elements)):
        temp = max(elements[i] + exclusive, inclusive)
        if inclusive > exclusive:
            exclusive = inclusive
        if temp > inclusive:
            inclusive = temp
    print inclusive


if __name__ == '__main__':
    arr = [4,1,1,4,5,1]
    find_max_sum(arr)