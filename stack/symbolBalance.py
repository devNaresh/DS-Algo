__author__ = 'naresh'

from stack import Stack


def matches(top, symbol):
    openingSymbols = "({["
    closingSymbols = ")}]"

    return openingSymbols.index(top) == closingSymbols.index(symbol)


def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced = 0
    for symbols in input:
        if symbols in ["(", "{", "["]:
            symbolstack.push(symbols)
        else:
            if symbolstack.head is None:
                balanced = 0
            else:
                topSymbol = symbolstack.pop()
                if not matches(topSymbol, symbols):
                    balanced = 0
                else:
                    balanced = 1

    return balanced


# def make_expression_balance(exp):
#     symbolstack = Stack()
#     for x in exp:
#         if x in ["(", "{", "["] or not matches(symbolstack.peek(), x):
#             symbolstack.push(x)
#         elif matches(symbolstack.peek(), x):
#             symbolstack.pop()


print checkSymbolBalance("([)]")
'''Output: 0'''

print checkSymbolBalance("{{([][])}()}")
'''Output: 1'''
