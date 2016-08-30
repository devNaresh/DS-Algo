__author__ = 'naresh'

from stack import Stack


def infixToPostFix(exp):
    prec = {}
    token = exp.split()
    stx = Stack()
    postfixList = []
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    for data in token:
        if data.isalpha():
            postfixList.append(data)
        else:
            if data == '(':
                stx.push(data)
            elif data in prec:
                if stx.is_empty():
                    stx.push(data)
                elif prec[stx.peek()] < prec[data]:
                    stx.push(data)
                else:
                    while stx.head is not None and prec[stx.peek()] >= prec[data]:
                        postfixList.append(stx.pop())
                    if not stx.is_empty() and stx.peek() == '(':
                        stx.pop()
                    stx.push(data)
            elif data == ")":
                while stx.head is not None and stx.peek() != '(':
                    postfixList.append(stx.pop())
                if not stx.is_empty() and stx.peek() == '(':
                    stx.pop()

    while not stx.is_empty():
        postfixList.append(stx.pop())

    return ' '.join(postfixList)


### BOOK Solution ##

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == '__main__':
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostFix("( A + B ) * C - ( D - E ) * ( F + G )"))
