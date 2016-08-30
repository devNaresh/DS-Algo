__author__ = '__naresh__'

# WAP to find number of possible binary tree with n number of nodes

"""
Use Catalan number formula

"""


def total_number_of_binary_tree(number_of_nodes):
    """Recursive Solution"""

    if number_of_nodes == 0:
        return 1
    else:
        total = 0
        for i in range(0, number_of_nodes):
            total += total_number_of_binary_tree(i) * total_number_of_binary_tree(number_of_nodes - 1 - i)
        return total


def total_number_of_binary_tree_DP(number_of_nodes):
    """Dynamic Programming Solution"""

    tree_memory = [0] * (number_of_nodes + 1)
    tree_memory[0] = tree_memory[1] = 1

    for i in range(2, number_of_nodes + 1):
        for j in range(0, i):
            tree_memory[i] += tree_memory[j] * tree_memory[i - j - 1]
    return tree_memory


if __name__ == "__main__":
    print total_number_of_binary_tree_DP(2)
