__author__ = "__naresh__"

# WAP to find total number of steps combination to reach at top of stair
# Condition -- You can only take 1 or 2 steps at a time

"""
Fibbnocci Series Solution

T[i] = T[i-1]+ T[i-2]

"""


def get_steps(nth_stair):
    """Recursive Solution"""
    if nth_stair <= 0:
        return [[1]]
    elif nth_stair == 1:
        return [[1, 1], [2]]
    elif nth_stair > 1:
        stair_1 = get_steps(nth_stair - 1)
        stair_2 = get_steps(nth_stair - 2)
        stair_1 = [x + [1] for x in stair_1]
        stair_2 = [x + [2] for x in stair_2]
        return stair_1 + stair_2


def get_steps_DP(nth_stair):
    """Dynamic Programming Solution"""
    stair_memory = [0] * (nth_stair + 1)
    stair_memory[0] = [[1]]
    stair_memory[1] = [[1, 1], [2]]

    for i in range(2, nth_stair + 1):
        stair_1 = [x + [1] for x in stair_memory[i - 1]]
        stair_2 = [x + [2] for x in stair_memory[i - 2]]
        stair_memory[i] = stair_1 + stair_2
    return stair_memory[nth_stair]


if __name__ == "__main__":
    print get_steps(6)
    print len(get_steps(6))
