


class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme
    def __str__(self):
        return f"{self.token_type}: {self.lexeme}"



class Lexer:
    def __init__(self, keywords, separators, operators, delimiters, numbers):
        self.keywords = (keywords)
        self.separators = (separators)
        self.operators = (operators)
        self.delimiters = (delimiters)
        self.numbers = (numbers)
        self.tokens = []

    def lexer(self, text):
            tokens = []
            i = 0
            while i < len(text):
                if text[i] in delimiters:
                    i += 1
                elif text[i].isdigit() or (text[i] == '.' and i + 1 < len(text) and text[i + 1].isdigit()):
                    number = text[i]
                    i += 1
                    while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                        number += text[i]
                        i += 1
                    if '.' in number:
                        tokens.append(Token("Float", float(number)))  # Token type "Float" for floating-point numbers
                    else:
                        tokens.append(Token("Integer", int(number)))  # Token type "Integer" for integers
                elif text[i].isalpha() or text[i] == '_':
                    identifier = text[i]
                    i += 1
                    while i < len(text) and (text[i].isalnum() or text[i] == '_'):
                        identifier += text[i]
                        i += 1
                    if identifier in self.keywords:
                        tokens.append(Token("Keyword", identifier))
                    else:
                        tokens.append(Token("Identifier", identifier))
                elif text[i] in self.operators:
                    tokens.append(Token("Operator", text[i]))
                    i += 1
                elif text[i] in self.separators:
                    tokens.append(Token("Separator", text[i]))
                    i += 1
                else:
                    i += 1
            self.tokens = tokens
            return tokens






keywords = ["as", "assert", "break", "class", "continue", 
        "def", "del", "elif", "else", "except",
        "False", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "None",
        "nonlocal", "not", "or", "pass", "raise",
        "return", "True", "try", "while", "with","yield"]

separators = ['\'', '(', ')', '{', '}', '[', ']', ',', '.', ':', ';']

operators = ['+', '-', '*', '/', '%', '&', '|', '>', '<', '=', '!']

delimiters = [' ', '+', '-', '*', '/', ',', ';', '>', '<', '=', '(', ')', '[', ']', '{', '}']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


