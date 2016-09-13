# WAP to find longest increasing subsequence


def longest_inc_sub_seq(data):
    length = len(data)
    temp = [1] * length

    for i in range(1, length):
        for j in range(i):
            if data[j] < data[i] and temp[i] < temp[j] + 1:
                temp[i] = temp[j] + 1
    print "Longest increasing subsequence is of length", max(temp)
if __name__ == "__main__":
    sequence = [3, 4, -1, 0, 5, 2, -2]
    longest_inc_sub_seq(sequence)
