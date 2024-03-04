import re # Used in regex functions
from tabulate import tabulate # Create tables

# Function to print error messages
def error_msg(error_Type, error_Token, errorLine):
    if error_Type == 'ERROR_INVALID_TOKEN':
        print(f'ERROR: {error_Type} {error_Token} IN LINE {errorLine}')
    else:
        print(f'ERROR: {error_Type} BUT NOT CLOSED IN LINE {errorLine}')


def build_regex():
    # All pascal regex in groups
    patternsPascal = [
        ('COMMENT', r'{[\S\s]*?}'),
        ('OPENNED_COMMENT', r'{[\S\s]*[^}]'),
        ('RESERVED_WORD', r'\b(program|var|integer|real|boolean|procedure|begin|end|if|then|else|while|do|not)\b'),
        ('BOOLEAN', r'\b(true|false)\b'),
        ('REAL', r'\b\d+\.\d*'),
        ('INTEGER', r'\b\d+\b'),
        ('ASSIGNMENT', r':='),
        ('RELATIONAL_OPERATOR', r'(<=|>=|<>|>|<|=)'),
        ('ADDITIVE_OPERATOR', r'(\+|-|\bor\b)'),
        ('MULTIPLICATION_OPERATOR', r'(\*|/|\band\b)'),
        ('IDENTIFIER', r'\b[a-zA-Z][a-zA-Z0-9_]*\b'),
        ('DELIMITER', r'[;.:\(\),]'),
        ('ERROR_INVALID_TOKEN',r'[^A-Za-z0-9=<>:;_\+\-\*\/{}\t\s.]')
    ]

    # Combine all regex groups using OR operator, compile and return the regex
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patternsPascal)
    regex = re.compile(combined_pattern)
    return regex

def match(dataInput):
    # Regex build to be used in matching loop
    regex = build_regex()

    # Result tokens and classifications
    tokens = []

    # tokens that don't will be in result
    nonListable_tokens = ('ERROR_INVALID_TOKEN', 'COMMENT', 'OPENNED_COMMENT')

    # Line and index used in lexer
    line = 1
    #index = 1 -> Can be useful in future...

    # For every match object in find iteration inside file data
    for match in regex.finditer(dataInput):
        # Get the start and end of match
        start, end = match.span()

        # Calculate line and index using newline char
        line += dataInput.count('\n', 0, start)
        # index = end - dataInput.rfind('\n', 0, start) -> Maybe in Future

        # If the match is a comment or error
        if match.lastgroup in nonListable_tokens:
            # if is an error... correct comment don't enter this statement
            if match.lastgroup != 'COMMENT':
                error_msg(match.lastgroup, match.group(), line)
            line = 1
            continue
        
        # Append in result list
        tokens.append((match.group(), match.lastgroup, str(line)))
        # Reset line for next loop
        line = 1
    # Return tokens, classification and line
    return tokens

# Using tabulate, creates a table with result tokens classification
def printTable(tokens):
    headers=['TOKEN ', 'CLASSIFICATION', 'LINE']
    table = tabulate(tokens ,headers=headers, tablefmt='grid')
    print(table)

# Open and close input file
def getProgramFile(fileInput):
    with open(fileInput, 'r') as opennedFile:
        data = opennedFile.read()
    return data

def lexer(fileInput):
    dataInput = getProgramFile(fileInput) # open input file
    tokens = match(dataInput) # Get tokens from main lexer function
    printTable(tokens) # Print token table
    return tokens # Return tokens to use in syntactic