# WAP to wrap words in line so that maximum width of lin not exceed 10

"""
Time Complexibility O(coins * total)
Space Complexibility O(coins * total)

******* Formula *******

1) First create 2D array of white spaces
2) create two array for position and cost
3) if arr[j][j] == INF
    cost[i] = arr[i][j-1] + cost[j] #should be minimum of i > j < length_of_arr
    position[i] = j + 1
   else:
       cost[i] = arr[i][j]
       position[i] = j + 1
"""

INF = 9999999999


def wrap_words(data):
    words = data.split()
    length = len(words)
    count_arr = [[0] * length for _ in range(length)]
    for i in range(length):
        max_len = 0
        for j in range(i, length):
            max_len += len(words[j]) + j - i
            if max_len <= 10:
                count_arr[i][j] = (10 - max_len)**2
            else:
                count_arr[i][j] = INF

    for x in count_arr:
        print x

    cost = [0] * length
    position = [0] * length
    for i in reversed(range(length)):
        if count_arr[i][length - 1] == INF:
            min_cost = count_arr[i][length - 1]
            for j in reversed(range(i, length)):
                if count_arr[i][j - 1] is not INF and \
                        count_arr[i][j - 1] + cost[j] < min_cost:
                    min_cost = count_arr[i][j - 1] + cost[j]
                    cost[i] = min_cost
                    position[i] = j + 1
        else:
            cost[i] = count_arr[i][j]
            position[i] = j + 1

    print "-" * 50
    old = 0
    for x in position:
        if words[old:x]:
            print " ".join(words[old:x])
        old = x

if __name__ == "__main__":
    line = "Tushar Roy likes to code"
    line2 = "My name is Naresh. What is your Name"
    wrap_words(line2)
