__author__ = '__naresh__'


def longest_Palindrome_Substring(string):
    n = len(string)
    if n == 0: return
    L = {}
    for i in range(n): L[(i, i)] = True
    for k in range(n - 1):
        for i in range(n):
            j = i + k
            if j >= n: continue
            if i + 1 <= j - 1:
                L[(i, j)] = L[(i + 1), (j - 1)] and string[i] == string[j]
            else:
                L[(i, j)] = string[i] == string[j]
    start, end = max([k for k in L if L[k]], key=lambda x: x[1] - x[0])
    return string[start: end + 1]

if __name__ == "__main__":
    print longest_Palindrome_Substring("")